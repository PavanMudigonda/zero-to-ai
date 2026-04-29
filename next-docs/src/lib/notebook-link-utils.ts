type NotebookCell = {
  cell_type?: string;
  source?: string | string[];
};

type NotebookDocument = {
  cells?: NotebookCell[];
  [key: string]: unknown;
};

declare global {
  interface Window {
    __ZERO_TO_AI_ROUTE_INDEX__?: string[];
  }
}

const MARKDOWN_LINK_PATTERN = /(\[[^\]]*\]\()([^\)]+)(\))/g;
const HTML_ATTRIBUTE_LINK_PATTERN = /((?:href|src)=['"])([^'"]+)(['"])/g;

function isExternalUrl(url: string): boolean {
  return /^(?:[a-z]+:)?\/\//i.test(url) || /^(?:mailto:|tel:|javascript:|data:|#)/i.test(url);
}

function splitTarget(url: string): { pathname: string; suffix: string } {
  const match = url.match(/^([^?#]*)(.*)$/);

  return {
    pathname: match?.[1] ?? url,
    suffix: match?.[2] ?? '',
  };
}

function ensureTrailingSlash(url: string): string {
  return url.endsWith('/') ? url : `${url}/`;
}

function normalizeSegmentName(segmentName: string): string {
  return segmentName.replace(/^[0-9]+[_-]?/, '').toLowerCase();
}

function routeDirectoryFromResolvedPath(resolvedRoutePath: string, rawTargetPath: string): string {
  if (!/\.(?:md|mdx|ipynb)$/i.test(rawTargetPath)) {
    return resolvedRoutePath;
  }

  const withoutExtension = resolvedRoutePath.replace(/\.(?:md|mdx|ipynb)$/i, '');

  if (/(?:^|\/)README(?:\.[A-Za-z0-9_-]+)?$/i.test(withoutExtension)) {
    return withoutExtension.replace(/(?:^|\/)README(?:\.[A-Za-z0-9_-]+)?$/i, '') || '/';
  }

  return withoutExtension;
}

function findSiblingAliasRoute(routeDirectory: string, routeIndex: string[]): string | null {
  const parentRoute = routeDirectory.replace(/\/[^/]+$/, '') || '/';
  const targetSegment = normalizeSegmentName(routeDirectory.split('/').filter(Boolean).pop() || '');

  for (const routePath of routeIndex) {
    const routeParent = routePath.replace(/\/[^/]+$/, '') || '/';
    const lastSegment = routePath.split('/').filter(Boolean).pop() || '';

    if (routeParent !== parentRoute) {
      continue;
    }

    if (normalizeSegmentName(lastSegment) === targetSegment) {
      return routePath;
    }
  }

  return null;
}

function normalizeNotebookTarget(targetUrl: string, currentPathname: string, routeIndex: string[]): string {
  if (!targetUrl || isExternalUrl(targetUrl)) {
    return targetUrl;
  }

  const { pathname: targetPathname, suffix } = splitTarget(targetUrl);

  if (!/\.(?:md|mdx|ipynb)$/i.test(targetPathname) && !targetUrl.endsWith('/')) {
    return targetUrl;
  }

  const resolvedRoutePath = new URL(targetPathname, `https://zero-to-ai.dev${ensureTrailingSlash(currentPathname || '/')}`).pathname;
  const candidateRouteDirectory = routeDirectoryFromResolvedPath(resolvedRoutePath, targetPathname);

  if (routeIndex.includes(candidateRouteDirectory)) {
    return `${ensureTrailingSlash(candidateRouteDirectory)}${suffix}`;
  }

  const siblingAliasRoute = findSiblingAliasRoute(candidateRouteDirectory, routeIndex);
  if (siblingAliasRoute) {
    return `${ensureTrailingSlash(siblingAliasRoute)}${suffix}`;
  }

  return targetUrl;
}

function normalizeLinkReferences(segment: string, pathname: string, routeIndex: string[]): string {
  const withMarkdownLinks = segment.replace(
    MARKDOWN_LINK_PATTERN,
    (_match, prefix: string, target: string, suffix: string) => `${prefix}${normalizeNotebookTarget(target, pathname, routeIndex)}${suffix}`,
  );

  return withMarkdownLinks.replace(
    HTML_ATTRIBUTE_LINK_PATTERN,
    (_match, prefix: string, target: string, suffix: string) => `${prefix}${normalizeNotebookTarget(target, pathname, routeIndex)}${suffix}`,
  );
}

function replaceOutsideCodeFences(text: string, replacer: (segment: string) => string): string {
  const segments = text.split(/(```[\s\S]*?```)/g);

  return segments
    .map((segment, index) => (index % 2 === 1 ? segment : replacer(segment)))
    .join('');
}

function normalizeMarkdownText(text: string, pathname: string, routeIndex: string[]): string {
  return replaceOutsideCodeFences(text, (segment) => {
    return normalizeLinkReferences(segment, pathname, routeIndex);
  });
}

export function normalizeNotebookLinks(
  ipynb: NotebookDocument,
  currentPathname: string,
  routeIndex: string[] = [],
): NotebookDocument {
  if (!Array.isArray(ipynb.cells)) {
    return ipynb;
  }

  return {
    ...ipynb,
    cells: ipynb.cells.map((cell) => {
      if (cell.cell_type !== 'markdown' || !cell.source) {
        return cell;
      }

      if (Array.isArray(cell.source)) {
        return {
          ...cell,
          source: cell.source.map((segment) => normalizeMarkdownText(segment, currentPathname, routeIndex)),
        };
      }

      return {
        ...cell,
        source: normalizeMarkdownText(cell.source, currentPathname, routeIndex),
      };
    }),
  };
}