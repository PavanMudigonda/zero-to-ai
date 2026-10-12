import { createRequire } from 'node:module';
import { mkdirSync, readdirSync, readFileSync, statSync, unlinkSync, writeFileSync } from 'node:fs';
import { dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer';
import { hashMermaidSource, normalizeMermaidSource } from '../src/lib/mermaid-source.mjs';

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const projectRoot = dirname(scriptDirectory);
const notebooksRoot = join(projectRoot, 'src', 'app');
const outputDirectory = join(projectRoot, 'public', 'notebook-mermaid');
const require = createRequire(import.meta.url);
const mermaidScriptPath = require.resolve('mermaid/dist/mermaid.min.js');
const mermaidFencePattern = /^[ \t]*```mermaid[ \t]*\r?\n([\s\S]*?)^[ \t]*```[ \t]*$/gim;

function collectNotebookPaths(directoryPath, notebookPaths = []) {
  for (const entryName of readdirSync(directoryPath)) {
    const absolutePath = join(directoryPath, entryName);
    const stats = statSync(absolutePath);

    if (stats.isDirectory()) {
      collectNotebookPaths(absolutePath, notebookPaths);
    } else if (entryName.endsWith('.ipynb')) {
      notebookPaths.push(absolutePath);
    }
  }

  return notebookPaths;
}

function extractMermaidSources(notebook) {
  const sources = [];

  for (const cell of notebook.cells ?? []) {
    if (cell.cell_type !== 'markdown') continue;

    const cellSource = Array.isArray(cell.source) ? cell.source.join('') : cell.source ?? '';
    mermaidFencePattern.lastIndex = 0;

    for (const match of cellSource.matchAll(mermaidFencePattern)) {
      const source = normalizeMermaidSource(match[1] ?? '');
      if (source) sources.push(source);
    }
  }

  return sources;
}

function setSvgIntrinsicDimensions(svg) {
  const viewBox = svg.match(/\bviewBox=["']([\d.eE+-]+)[ ,]+([\d.eE+-]+)[ ,]+([\d.eE+-]+)[ ,]+([\d.eE+-]+)["']/i);
  if (!viewBox) {
    throw new Error('Mermaid returned an SVG without a valid viewBox.');
  }

  const [, , , width, height] = viewBox;
  const svgRoot = svg.match(/<svg\b([^>]*)>/i);
  if (!svgRoot) {
    throw new Error('Mermaid returned malformed SVG markup.');
  }

  const rootAttributes = svgRoot[1].replace(/\s(?:width|height|style)=["'][^"']*["']/gi, '');
  const normalizedRoot = `<svg${rootAttributes} width="${width}" height="${height}">`;
  return svg.replace(svgRoot[0], normalizedRoot);
}

async function renderSvg(page, source, diagramId) {
  return page.evaluate(
    async ({ diagramSource, id }) => {
      const { svg } = await window.mermaid.render(id, diagramSource);
      return svg;
    },
    { diagramSource: source, id: diagramId },
  );
}

async function main() {
  mkdirSync(outputDirectory, { recursive: true });

  for (const entryName of readdirSync(outputDirectory)) {
    const outputPath = join(outputDirectory, entryName);
    if (entryName.endsWith('.svg') && statSync(outputPath).isFile()) {
      unlinkSync(outputPath);
    }
  }

  const notebookPaths = collectNotebookPaths(notebooksRoot);
  const diagrams = new Map();

  for (const notebookPath of notebookPaths) {
    const notebook = JSON.parse(readFileSync(notebookPath, 'utf8'));
    for (const source of extractMermaidSources(notebook)) {
      const hash = await hashMermaidSource(source);
      if (!diagrams.has(hash)) {
        diagrams.set(hash, { notebookPath, source });
      }
    }
  }

  const renderingErrors = [];
  const browser = await puppeteer.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.setContent('<!doctype html><html><body></body></html>');
    await page.addScriptTag({ path: mermaidScriptPath });
    await page.evaluate(() => {
      window.mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' });
    });

    for (const [hash, { notebookPath, source }] of diagrams) {
      const diagramId = `notebook-mermaid-${hash}`;
      try {
        const svg = await renderSvg(page, source, diagramId);
        writeFileSync(join(outputDirectory, `${hash}.svg`), setSvgIntrinsicDimensions(svg));
      } catch (error) {
        const notebookRelativePath = relative(projectRoot, notebookPath).split(sep).join('/');
        const message = error instanceof Error ? error.message : String(error);
        renderingErrors.push(`${notebookRelativePath}: ${message}`);
      }
    }
  } finally {
    await browser.close();
  }

  if (renderingErrors.length > 0) {
    throw new Error(
      `Failed to render ${renderingErrors.length} Mermaid diagram(s):\n${renderingErrors.join('\n')}`,
    );
  }

  console.info(`Generated ${diagrams.size} Mermaid SVG assets from ${notebookPaths.length} notebooks.`);
}

await main();
