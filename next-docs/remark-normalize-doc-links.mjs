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

function stripTrailingSlash(url) {
  return url !== '/' ? url.replace(/\/+$/, '') : '/';
}

function normalizeSegmentName(segmentName) {
  let decodedSegmentName = segmentName;

  try {
    decodedSegmentName = decodeURIComponent(segmentName);
  } catch {
    decodedSegmentName = segmentName;
  }

  const normalizedTokens = decodedSegmentName
    .replace(/\.(?:md|mdx|ipynb)$/i, '')
    .toLowerCase()
    .split(/[^a-z0-9]+/i)
    .filter(Boolean)
    .filter((token) => !/^\d+$/.test(token));

  return normalizedTokens.filter((token, index) => index === 0 || token !== normalizedTokens[index - 1]).join('');
}

function routeDirectory(routePath) {
  const segments = routePath.replace(/\/+$/, '').split('/').filter(Boolean);

  if (segments.length <= 1) {
    return '/';
  }

  return `/${segments.slice(0, -1).join('/')}`;
}

function routePathFromSourceFile(sourceFilePath) {
  const relativePath = path.relative(APP_ROOT, sourceFilePath).replaceAll(path.sep, '/');

  if (/\/page\.[^.]+$/i.test(relativePath) || /^page\.[^.]+$/i.test(relativePath)) {
    const routeDirectory = path.posix.dirname(relativePath);
    return routeDirectory === '.' ? '/' : `/${routeDirectory}`;
  }

  return `/${relativePath.replace(/\.(?:md|mdx|ipynb)$/i, '')}`;
}

function canonicalRoutePathFromSourceFile(sourceFilePath) {
  const sourceRoutePath = routePathFromSourceFile(sourceFilePath);
  const routeBasename = path.posix.basename(sourceRoutePath);
  const parentRoutePath = path.posix.dirname(sourceRoutePath) || '/';
  const parentBasename = path.posix.basename(parentRoutePath);

  if (/\/page\.[^.]+$/i.test(sourceFilePath) || /^page\.[^.]+$/i.test(path.posix.basename(sourceFilePath))) {
    return sourceRoutePath;
  }

  if (routeBasename && parentBasename && routeBasename === parentBasename) {
    return parentRoutePath;
  }

  return sourceRoutePath;
}

function candidateBasePathsFromSourceFile(sourceFilePath) {
  const canonicalRoutePath = canonicalRoutePathFromSourceFile(sourceFilePath);
  const parentRoutePath = routeDirectory(canonicalRoutePath);
  const grandparentRoutePath = routeDirectory(parentRoutePath);

  return [...new Set([canonicalRoutePath, parentRoutePath, grandparentRoutePath])];
}

function routeDirectoryFromResolvedPath(resolvedRoutePath, rawTargetPath) {
  if (!path.extname(rawTargetPath)) {
    return stripTrailingSlash(resolvedRoutePath) || '/';
  }

  const parsedTarget = path.posix.parse(resolvedRoutePath);

  if (/^README(?:\.[A-Za-z0-9_-]+)?$/i.test(parsedTarget.name)) {
    return parsedTarget.dir || '/';
  }

  return stripTrailingSlash(`${parsedTarget.dir}/${parsedTarget.name}`.replace(/\/+/g, '/')) || '/';
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

function findNearestAncestorAliasRoute(routeDirectoryPath) {
  const targetSlug = normalizeSegmentName(path.posix.basename(routeDirectoryPath));
  let ancestorRouteDirectory = path.posix.dirname(routeDirectoryPath) || '/';

  while (ancestorRouteDirectory && ancestorRouteDirectory !== '/') {
    const parentRouteDirectory = path.posix.dirname(ancestorRouteDirectory) || '/';
    const ancestorAliasRoute = routeIndex.aliasRouteLookup.get(`${parentRouteDirectory}|${targetSlug}`);

    if (ancestorAliasRoute) {
      return ancestorAliasRoute;
    }

    ancestorRouteDirectory = parentRouteDirectory;
  }

  return null;
}

function findNotebookFallbackRoute(routeDirectoryPath) {
  const notebookRoute = `${stripTrailingSlash(routeDirectoryPath) || '/'}/notebook`.replace(/\/+/g, '/');

  if (routeIndex.routePaths.has(notebookRoute)) {
    return notebookRoute;
  }

  const siblingAliasRoute = findSiblingAliasRoute(notebookRoute);
  if (siblingAliasRoute) {
    return siblingAliasRoute;
  }

  return findNearestAncestorAliasRoute(notebookRoute);
}

function findParentIndexRoute(sourceBasePath) {
  const parentRoutePath = routeDirectory(sourceBasePath);

  if (routeIndex.routePaths.has(parentRoutePath)) {
    return parentRoutePath;
  }

  return null;
}

function normalizeLinkTarget(targetUrl, sourceFilePath) {
  if (!targetUrl || isExternalUrl(targetUrl)) {
    return targetUrl;
  }

  const { pathname: targetPathname, suffix } = splitTarget(targetUrl);
  for (const linkBasePath of candidateBasePathsFromSourceFile(sourceFilePath)) {
    const resolvedRoutePath = new URL(
      targetPathname,
      `https://zero-to-ai.dev${ensureTrailingSlash(linkBasePath)}`,
    ).pathname;
    const candidateRouteDirectory = routeDirectoryFromResolvedPath(resolvedRoutePath, targetPathname);

    if (routeIndex.routePaths.has(candidateRouteDirectory)) {
      return toRelativeRouteUrl(sourceFilePath, candidateRouteDirectory, suffix);
    }

    if (/(?:^|\/)Index\.ipynb$/i.test(targetPathname)) {
      const parentIndexRoute = findParentIndexRoute(linkBasePath);
      if (parentIndexRoute) {
        return toRelativeRouteUrl(sourceFilePath, parentIndexRoute, suffix);
      }
    }

    const siblingAliasRoute = findSiblingAliasRoute(candidateRouteDirectory);
    if (siblingAliasRoute) {
      return toRelativeRouteUrl(sourceFilePath, siblingAliasRoute, suffix);
    }

    const ancestorAliasRoute = findNearestAncestorAliasRoute(candidateRouteDirectory);
    if (ancestorAliasRoute) {
      return toRelativeRouteUrl(sourceFilePath, ancestorAliasRoute, suffix);
    }

    if (/(?:^|\/)README(?:\.[A-Za-z0-9_-]+)?\.(?:md|mdx)$/i.test(targetPathname)) {
      const notebookFallbackRoute = findNotebookFallbackRoute(candidateRouteDirectory);
      if (notebookFallbackRoute) {
        return toRelativeRouteUrl(sourceFilePath, notebookFallbackRoute, suffix);
      }
    }
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