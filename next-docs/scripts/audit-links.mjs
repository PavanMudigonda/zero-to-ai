import fs from 'node:fs';
import path from 'node:path';

const APP_ROOT = path.join(process.cwd(), 'src', 'app');
const DOC_EXTENSIONS = new Set(['.md', '.mdx', '.ipynb']);
const PAGE_FILE_NAMES = new Set(['page.mdx', 'page.tsx', 'page.ts', 'page.jsx', 'page.js']);
const MARKDOWN_LINK_PATTERN = /\[[^\]]*\]\(([^)]+)\)/g;
const HTML_ATTRIBUTE_LINK_PATTERN = /(?:href|src)=['"]([^'"]+)['"]/g;

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

function ensureTrailingSlash(url) {
  return url.endsWith('/') ? url : `${url}/`;
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

function findSiblingAliasRoute(routeDirectoryPath) {
  const parentRouteDirectory = path.posix.dirname(routeDirectoryPath);
  const targetSlug = normalizeSegmentName(path.posix.basename(routeDirectoryPath));

  return routeIndex.aliasRouteLookup.get(`${parentRouteDirectory}|${targetSlug}`) ?? null;
}

function isResolvableDocTarget(targetUrl, sourceFilePath) {
  if (!targetUrl || isExternalUrl(targetUrl)) {
    return true;
  }

  const { pathname: targetPathname } = splitTarget(targetUrl);
  const resolvedRoutePath = resolveRoutePath(targetPathname, sourceFilePath);
  const candidateRouteDirectory = routeDirectoryFromResolvedPath(resolvedRoutePath, targetPathname);

  if (!path.extname(targetPathname)) {
    return routeIndex.routePaths.has(candidateRouteDirectory);
  }

  if (!DOC_EXTENSIONS.has(path.extname(targetPathname).toLowerCase())) {
    return true;
  }

  if (routeIndex.routePaths.has(candidateRouteDirectory)) {
    return true;
  }

  return Boolean(findSiblingAliasRoute(candidateRouteDirectory));
}

function walkFiles(currentDirectory, results) {
  for (const entryName of fs.readdirSync(currentDirectory)) {
    const absolutePath = path.join(currentDirectory, entryName);
    const stats = fs.statSync(absolutePath);

    if (stats.isDirectory()) {
      walkFiles(absolutePath, results);
      continue;
    }

    if (entryName === 'page.mdx' || entryName.endsWith('.ipynb')) {
      results.push(absolutePath);
    }
  }
}

function collectLinksFromMarkdown(text) {
  const links = [];

  for (const match of text.matchAll(MARKDOWN_LINK_PATTERN)) {
    links.push(match[1]);
  }

  for (const match of text.matchAll(HTML_ATTRIBUTE_LINK_PATTERN)) {
    links.push(match[1]);
  }

  return links;
}

function collectFileLinks(filePath) {
  if (filePath.endsWith('.ipynb')) {
    const notebook = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const markdownSources = (notebook.cells || [])
      .filter((cell) => cell.cell_type === 'markdown')
      .flatMap((cell) => Array.isArray(cell.source) ? cell.source : [cell.source || '']);

    return markdownSources.flatMap((source) => collectLinksFromMarkdown(String(source)));
  }

  return collectLinksFromMarkdown(fs.readFileSync(filePath, 'utf8'));
}

const sourceFiles = [];
walkFiles(APP_ROOT, sourceFiles);

const brokenTargets = [];

for (const sourceFilePath of sourceFiles) {
  for (const targetUrl of collectFileLinks(sourceFilePath)) {
    if (!isResolvableDocTarget(targetUrl, sourceFilePath)) {
      brokenTargets.push({
        source: path.relative(process.cwd(), sourceFilePath),
        target: targetUrl,
      });
    }
  }
}

if (!brokenTargets.length) {
  console.log('No unresolved documentation links found.');
  process.exit(0);
}

console.log(`Unresolved documentation links: ${brokenTargets.length}`);
for (const brokenTarget of brokenTargets) {
  console.log(`${brokenTarget.source} -> ${brokenTarget.target}`);
}

process.exit(1);