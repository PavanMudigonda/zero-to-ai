import { readdirSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const APP_ROOT = join(process.cwd(), 'src', 'app');
const PAGE_FILE_NAMES = new Set(['page.mdx', 'page.tsx', 'page.ts', 'page.jsx', 'page.js']);
const EXCLUDED_SEGMENTS = new Set(['_meta.ts', 'error.tsx', 'not-found.tsx', 'layout.tsx']);
const EXCLUDED_TOP_LEVEL_SEGMENTS = new Set(['app', 'auth', 'demo', 'login']);
const EXCLUDED_ROUTE_PREFIXES = ['/32-cheatsheets/system-design'];
let cachedAllRoutes: string[] | null = null;
let cachedCanonicalRoutes: string[] | null = null;

function shouldExcludeTopLevelRoute(route: string): boolean {
  const [firstSegment] = route.split('/').filter(Boolean);
  return Boolean(firstSegment && EXCLUDED_TOP_LEVEL_SEGMENTS.has(firstSegment));
}

function shouldExcludeRoutePrefix(route: string): boolean {
  return EXCLUDED_ROUTE_PREFIXES.some((prefix) => route === prefix || route.startsWith(`${prefix}/`));
}

function shouldSkipSelfNestedRoute(route: string): boolean {
  const segments = route.split('/').filter(Boolean);

  if (segments.length < 2) {
    return false;
  }

  for (let index = 1; index < segments.length; index += 1) {
    if (segments[index] === segments[index - 1]) {
      return true;
    }
  }

  return false;
}

function collectRouteDirectories(currentDirectory: string, routeDirectories: string[]) {
  for (const entryName of readdirSync(currentDirectory)) {
    if (EXCLUDED_SEGMENTS.has(entryName)) {
      continue;
    }

    const absolutePath = join(currentDirectory, entryName);
    const stats = statSync(absolutePath);

    if (stats.isDirectory()) {
      collectRouteDirectories(absolutePath, routeDirectories);
      continue;
    }

    if (PAGE_FILE_NAMES.has(entryName)) {
      routeDirectories.push(currentDirectory);
    }
  }
}

function collectStaticSiteRoutes(): string[] {
  if (cachedAllRoutes) {
    return cachedAllRoutes;
  }

  const routeDirectories: string[] = [];
  collectRouteDirectories(APP_ROOT, routeDirectories);

  cachedAllRoutes = [...new Set(routeDirectories)]
    .map((directoryPath) => {
      const relativeDirectory = relative(APP_ROOT, directoryPath).replaceAll(sep, '/');
      return relativeDirectory ? `/${relativeDirectory}` : '/';
    })
    .filter((route) => !shouldExcludeTopLevelRoute(route))
    .filter((route) => !shouldExcludeRoutePrefix(route))
    .sort((left, right) => left.localeCompare(right));

  return cachedAllRoutes;
}

export function getStaticSiteRoutes(options?: { includeSelfNestedRoutes?: boolean }): string[] {
  if (options?.includeSelfNestedRoutes) {
    return collectStaticSiteRoutes();
  }

  if (cachedCanonicalRoutes) {
    return cachedCanonicalRoutes;
  }

  cachedCanonicalRoutes = collectStaticSiteRoutes()
    .filter((route) => !shouldSkipSelfNestedRoute(route))
    .sort((left, right) => left.localeCompare(right));

  return cachedCanonicalRoutes;
}