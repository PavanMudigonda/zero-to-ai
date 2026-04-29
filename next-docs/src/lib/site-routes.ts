import { readdirSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const APP_ROOT = join(process.cwd(), 'src', 'app');
const PAGE_FILE_NAMES = new Set(['page.mdx', 'page.tsx', 'page.ts', 'page.jsx', 'page.js']);
const EXCLUDED_SEGMENTS = new Set(['_meta.ts', 'error.tsx', 'not-found.tsx', 'layout.tsx']);
let cachedRoutes: string[] | null = null;

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

export function getStaticSiteRoutes(): string[] {
  if (cachedRoutes) {
    return cachedRoutes;
  }

  const routeDirectories: string[] = [];
  collectRouteDirectories(APP_ROOT, routeDirectories);

  cachedRoutes = [...new Set(routeDirectories)]
    .map((directoryPath) => {
      const relativeDirectory = relative(APP_ROOT, directoryPath).replaceAll(sep, '/');
      return relativeDirectory ? `/${relativeDirectory}` : '/';
    })
    .sort((left, right) => left.localeCompare(right));

  return cachedRoutes;
}