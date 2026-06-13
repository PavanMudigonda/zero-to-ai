import { mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const projectRoot = dirname(scriptDirectory);
const appRoot = join(projectRoot, 'src', 'app');
const outputPath = join(projectRoot, 'public', 'route-index.json');
const moduleOutputPath = join(projectRoot, 'src', 'generated', 'route-index.ts');
const pageFileNames = new Set(['page.mdx', 'page.tsx', 'page.ts', 'page.jsx', 'page.js']);
const excludedSegments = new Set(['_meta.ts', 'error.tsx', 'not-found.tsx', 'layout.tsx']);
const excludedTopLevelSegments = new Set(['app', 'auth', 'demo', 'login']);

function shouldSkipSelfNestedRoute(route) {
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

function shouldExcludeTopLevelRoute(route) {
  const [firstSegment] = route.split('/').filter(Boolean);
  return Boolean(firstSegment && excludedTopLevelSegments.has(firstSegment));
}

function collectRouteDirectories(currentDirectory, routeDirectories) {
  for (const entryName of readdirSync(currentDirectory)) {
    if (excludedSegments.has(entryName)) {
      continue;
    }

    const absolutePath = join(currentDirectory, entryName);
    const stats = statSync(absolutePath);

    if (stats.isDirectory()) {
      collectRouteDirectories(absolutePath, routeDirectories);
      continue;
    }

    if (!pageFileNames.has(entryName)) {
      continue;
    }

    if (entryName === 'page.mdx') {
      const fileContents = readFileSync(absolutePath, 'utf8');

      if (!fileContents.includes('<DynamicNotebook')) {
        continue;
      }
    }

    routeDirectories.push(currentDirectory);
  }
}

const routeDirectories = [];
collectRouteDirectories(appRoot, routeDirectories);

const notebookRoutes = [...new Set(routeDirectories)]
  .map((directoryPath) => {
    const relativeDirectory = relative(appRoot, directoryPath).replaceAll(sep, '/');
    return relativeDirectory ? `/${relativeDirectory}` : '/';
  })
  .filter((route) => !shouldExcludeTopLevelRoute(route))
  .filter((route) => !shouldSkipSelfNestedRoute(route))
  .sort((left, right) => left.localeCompare(right));

mkdirSync(dirname(outputPath), { recursive: true });
writeFileSync(outputPath, `${JSON.stringify(notebookRoutes)}\n`);

mkdirSync(dirname(moduleOutputPath), { recursive: true });
writeFileSync(
  moduleOutputPath,
  [
    'export const generatedRouteIndex = Object.freeze(',
    `  ${JSON.stringify(notebookRoutes, null, 2)}`,
    ');',
    '',
    'export default generatedRouteIndex;',
    '',
  ].join('\n'),
);