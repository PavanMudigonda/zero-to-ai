import fs from 'node:fs';
import path from 'node:path';

const DOC_EXTENSIONS = new Set(['.md', '.mdx', '.ipynb']);
const APP_ROOT = path.join(process.cwd(), 'src', 'app');
const PAGE_FILE_NAMES = new Set(['page.mdx', 'page.tsx', 'page.ts', 'page.jsx', 'page.js']);

function collectRouteDirectories(currentDirectoryPath, routeDirectories) {
  for (const entryName of fs.readdirSync(currentDirectoryPath)) {
    const absolutePath = path.join(currentDirectoryPath, entryName);
    const stats = fs.statSync(absolutePath);

    if (stats.isDirectory()) {
      collectRouteDirectories(absolutePath, routeDirectories);
      continue;
    }

    if (PAGE_FILE_NAMES.has(entryName)) {
      const relativeDirectory = path.relative(APP_ROOT, currentDirectoryPath).replaceAll(path.sep, '/');
      routeDirectories.add(relativeDirectory ? `/${relativeDirectory}` : '/');
    }
  }
}

function buildRouteIndex() {
  const routePaths = new Set();
  collectRouteDirectories(APP_ROOT, routePaths);

  const aliasRouteLookup = new Map();

  for (const routePath of routePaths) {
    const parentRoutePath = path.posix.dirname(routePath);
    const routeSegment = path.posix.basename(routePath);
    const aliasKey = `${parentRoutePath}|${normalizeSegmentName(routeSegment)}`;

    if (!aliasRouteLookup.has(aliasKey)) {
      aliasRouteLookup.set(aliasKey, routePath);
    }
  }

  return {
    routePaths,
    aliasRouteLookup,
  };
}

const routeIndex = buildRouteIndex();

function isExternalUrl(url) {
  return /^(?:[a-z]+:)?\/\//i.test(url) || /^(?:mailto:|tel:|javascript:|data:|#)/i.test(url);
}

function splitTarget(url) {
  const match = url.match(/^([^?#]*)(.*)$/);

  return {
    pathname: match?.[1] ?? url,
    suffix: match?.[2] ?? '',
  };
}

function usesDocExtension(targetPath) {
  return DOC_EXTENSIONS.has(path.extname(targetPath).toLowerCase());
}

function ensureTrailingSlash(url) {
  return url.endsWith('/') ? url : `${url}/`;
}

function normalizeSegmentName(segmentName) {
  return segmentName.replace(/^[0-9]+[_-]?/, '').toLowerCase();
}

function routePathFromSourceFile(sourceFilePath) {
  const relativePath = path.relative(APP_ROOT, sourceFilePath).replaceAll(path.sep, '/');

  if (/\/page\.[^.]+$/i.test(relativePath) || /^page\.[^.]+$/i.test(relativePath)) {
    const routeDirectory = path.posix.dirname(relativePath);
    return routeDirectory === '.' ? '/' : `/${routeDirectory}`;
  }

  return `/${relativePath.replace(/\.(?:md|mdx|ipynb)$/i, '')}`;
}

function resolveRoutePath(targetPathname, sourceFilePath) {
  const sourceRoutePath = routePathFromSourceFile(sourceFilePath);
  return new URL(targetPathname, `https://zero-to-ai.dev${ensureTrailingSlash(sourceRoutePath)}`).pathname;
}

function routeDirectoryFromResolvedPath(resolvedRoutePath, rawTargetPath) {
  if (!path.extname(rawTargetPath)) {
    return resolvedRoutePath;
  }

  const parsedTarget = path.posix.parse(resolvedRoutePath);

  if (/^README(?:\.[A-Za-z0-9_-]+)?$/i.test(parsedTarget.name)) {
    return parsedTarget.dir || '/';
  }

  return `${parsedTarget.dir}/${parsedTarget.name}`.replace(/\/+/g, '/');
}

function toRelativeRouteUrl(sourceFilePath, routeDirectoryPath, suffix) {
  const sourceRoutePath = routePathFromSourceFile(sourceFilePath);
  let relativePath = path.posix.relative(path.posix.dirname(sourceRoutePath), routeDirectoryPath);

  if (!relativePath) {
    relativePath = '.';
  } else if (!relativePath.startsWith('.')) {
    relativePath = `./${relativePath}`;
  }

  return `${ensureTrailingSlash(relativePath)}${suffix}`;
}

function findSiblingAliasRoute(routeDirectoryPath) {
  const parentRouteDirectory = path.posix.dirname(routeDirectoryPath);
  const targetSlug = normalizeSegmentName(path.posix.basename(routeDirectoryPath));

  return routeIndex.aliasRouteLookup.get(`${parentRouteDirectory}|${targetSlug}`) ?? null;
}

function normalizeLinkTarget(targetUrl, sourceFilePath) {
  if (!targetUrl || isExternalUrl(targetUrl)) {
    return targetUrl;
  }

  const { pathname: targetPathname, suffix } = splitTarget(targetUrl);
  const resolvedRoutePath = resolveRoutePath(targetPathname, sourceFilePath);
  const candidateRouteDirectory = routeDirectoryFromResolvedPath(resolvedRoutePath, targetPathname);

  if (routeIndex.routePaths.has(candidateRouteDirectory)) {
    return toRelativeRouteUrl(sourceFilePath, candidateRouteDirectory, suffix);
  }

  const siblingAliasRoute = findSiblingAliasRoute(candidateRouteDirectory);
  if (siblingAliasRoute) {
    return toRelativeRouteUrl(sourceFilePath, siblingAliasRoute, suffix);
  }

  return targetUrl;
}

function normalizeNodeLinks(node, sourceFilePath) {
  if (!node || typeof node !== 'object') {
    return;
  }

  if ((node.type === 'link' || node.type === 'definition') && typeof node.url === 'string') {
    node.url = normalizeLinkTarget(node.url, sourceFilePath);
  }

  if ((node.type === 'mdxJsxTextElement' || node.type === 'mdxJsxFlowElement') && Array.isArray(node.attributes)) {
    for (const attribute of node.attributes) {
      if (
        attribute &&
        typeof attribute === 'object' &&
        (attribute.name === 'href' || attribute.name === 'src') &&
        typeof attribute.value === 'string'
      ) {
        attribute.value = normalizeLinkTarget(attribute.value, sourceFilePath);
      }
    }
  }

  if (Array.isArray(node.children)) {
    for (const child of node.children) {
      normalizeNodeLinks(child, sourceFilePath);
    }
  }
}

export default function remarkNormalizeDocLinks() {
  return (tree, file) => {
    const sourceFilePath = file?.path ? String(file.path) : '';
    normalizeNodeLinks(tree, sourceFilePath);
  };
}