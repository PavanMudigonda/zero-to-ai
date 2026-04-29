import { mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const projectRoot = dirname(scriptDirectory);
const appRoot = join(projectRoot, 'src', 'app');
const outputPath = join(projectRoot, 'public', 'route-index.json');
const pageFileNames = new Set(['page.mdx', 'page.tsx', 'page.ts', 'page.jsx', 'page.js']);
const excludedSegments = new Set(['_meta.ts', 'error.tsx', 'not-found.tsx', 'layout.tsx']);

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
  .sort((left, right) => left.localeCompare(right));

mkdirSync(dirname(outputPath), { recursive: true });
writeFileSync(outputPath, `${JSON.stringify(notebookRoutes)}\n`);