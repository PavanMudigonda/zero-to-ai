import fs from 'node:fs';
import path from 'node:path';

const LIVE_SITE = 'https://zero-to-ai.dev';
const GITHUB_REPO = 'https://github.com/PavanMudigonda/zero-to-ai';

function isLocalUrl(url) {
  return url && !/^(?:[a-z]+:)?\/\//i.test(url) && !/^(?:mailto:|tel:|javascript:|data:|#)/i.test(url);
}

function splitUrl(url) {
  const hashIdx = url.indexOf('#');
  const queryIdx = url.indexOf('?');
  const cutoffs = [hashIdx, queryIdx].filter((i) => i >= 0);
  const cutoff = cutoffs.length ? Math.min(...cutoffs) : url.length;
  return { pathPart: url.slice(0, cutoff), suffix: url.slice(cutoff) };
}

function resolveLocalPath(target, filePath) {
  if (!target || !filePath) return null;
  if (target.startsWith('/')) {
    return path.join(process.cwd(), 'public', target.slice(1));
  }
  return path.resolve(path.dirname(filePath), target);
}

// Derive the live-site route slug for an MDX file, e.g.
// .../next-docs/src/app/00-course-setup/page.mdx → "00-course-setup"
// .../next-docs/src/app/03-maths/foundational/page.mdx → "03-maths/foundational"
function currentRouteSlug(filePath) {
  if (!filePath) return null;
  const marker = '/next-docs/src/app/';
  const idx = filePath.indexOf(marker);
  if (idx < 0) return null;
  const rel = filePath.slice(idx + marker.length);
  // Drop trailing /page.mdx (or .md/.mdx file segment)
  const dir = rel.replace(/\/page\.(md|mdx|tsx|jsx)$/i, '');
  return dir.replace(/\/+$/, '') || null;
}

// Rewrite known curriculum paths to live-site URLs. Returns a new URL or null.
function tryRewrite(url, filePath) {
  const { pathPart, suffix } = splitUrl(url);

  // ../NN-phase/.../file.md or .ipynb → /NN-phase/.../file
  const phaseMatch = pathPart.match(/^(?:\.{1,2}\/)+(\d{2}-[a-z][a-z0-9-]*)\/(.*)$/i);
  if (phaseMatch) {
    const phase = phaseMatch[1];
    let rest = phaseMatch[2].replace(/\.(md|mdx|ipynb)$/i, '');
    rest = rest.replace(/(^|\/)README$/i, '');
    rest = rest.replace(/\/+$/, '');
    const slug = rest ? `${phase}/${rest}` : phase;
    return `${LIVE_SITE}/${slug}${suffix}`;
  }

  // ../README.md or ./README.md or README.md at repo root → GitHub repo
  if (/^(?:\.{1,2}\/)*README\.md$/i.test(pathPart)) {
    return `${GITHUB_REPO}${suffix}`;
  }

  // Same-directory refs ./foo.md or foo.md → resolve against the current page's route.
  // Next.js app-router publishes a directory at /<current-route>/<foo>, even though the
  // literal file foo.md doesn't sit beside the source page.mdx.
  const sameDirMatch = pathPart.match(/^\.?\/?([^/]+)\.(md|mdx|ipynb)$/i);
  if (sameDirMatch) {
    const slug = currentRouteSlug(filePath);
    if (slug) {
      const name = sameDirMatch[1].replace(/^README$/i, '');
      if (!name) return `${LIVE_SITE}/${slug}${suffix}`;
      return `${LIVE_SITE}/${slug}/${name}${suffix}`;
    }
  }

  return null;
}

function extractText(node) {
  if (!node) return '';
  if (node.type === 'text' || node.type === 'inlineCode') return node.value || '';
  if (Array.isArray(node.children)) {
    return node.children.map(extractText).join('');
  }
  return '';
}

function shouldHandleLink(url) {
  if (!isLocalUrl(url)) return false;
  // Only act on refs that look like file paths. Pure fragments/anchors handled by isLocalUrl above.
  return /\.(md|mdx|ipynb)(?:$|[#?])/i.test(url);
}

function fixNode(node, filePath) {
  if (!node || typeof node !== 'object') return;

  // Images: keep prior behavior — strip if local target missing.
  if (node.type === 'image' && typeof node.url === 'string' && isLocalUrl(node.url)) {
    const { pathPart } = splitUrl(node.url);
    const resolved = resolveLocalPath(pathPart, filePath);
    if (resolved && !fs.existsSync(resolved)) {
      node.type = 'text';
      node.value = node.alt || 'Image unavailable in this repo snapshot.';
      delete node.url;
      delete node.title;
      delete node.alt;
    }
  }

  // Links to .md/.mdx/.ipynb: rewrite to live-site URLs where we can, otherwise convert to plain text.
  if (node.type === 'link' && typeof node.url === 'string' && shouldHandleLink(node.url)) {
    const { pathPart } = splitUrl(node.url);
    const resolved = resolveLocalPath(pathPart, filePath);
    const exists = resolved ? fs.existsSync(resolved) : false;

    if (!exists) {
      const rewritten = tryRewrite(node.url, filePath);
      if (rewritten) {
        node.url = rewritten;
      } else {
        const text = extractText(node) || node.title || node.url;
        node.type = 'text';
        node.value = text;
        delete node.url;
        delete node.title;
        delete node.children;
      }
    }
  }

  if (Array.isArray(node.children)) {
    for (const child of node.children) fixNode(child, filePath);
  }
}

export default function remarkFixMissingRefs() {
  return (tree, file) => {
    fixNode(tree, file?.path ? String(file.path) : '');
  };
}
