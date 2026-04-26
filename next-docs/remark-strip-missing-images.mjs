import fs from 'node:fs';
import path from 'node:path';

const IMAGE_EXTENSIONS = new Set([
  '.apng',
  '.avif',
  '.gif',
  '.jpeg',
  '.jpg',
  '.png',
  '.svg',
  '.webp'
]);

function isLocalUrl(url) {
  return url && !/^(?:[a-z]+:)?\/\//i.test(url) && !/^(?:mailto:|tel:|javascript:|data:|#)/i.test(url);
}

function normalizeTarget(url) {
  return url.split('#', 1)[0].split('?', 1)[0];
}

function resolveImagePath(target, filePath) {
  if (!target || !filePath) {
    return null;
  }

  if (target.startsWith('/')) {
    return path.join(process.cwd(), 'public', target.slice(1));
  }

  return path.resolve(path.dirname(filePath), target);
}

function replaceMissingImages(node, filePath) {
  if (!node || typeof node !== 'object') {
    return;
  }

  if (node.type === 'image' && typeof node.url === 'string' && isLocalUrl(node.url)) {
    const target = normalizeTarget(node.url);
    const extension = path.extname(target).toLowerCase();

    if (IMAGE_EXTENSIONS.has(extension)) {
      const resolvedPath = resolveImagePath(target, filePath);

      if (resolvedPath && !fs.existsSync(resolvedPath)) {
        node.type = 'text';
        node.value = node.alt || 'Image unavailable in this repo snapshot.';
        delete node.url;
        delete node.title;
        delete node.alt;
      }
    }
  }

  if (Array.isArray(node.children)) {
    for (const child of node.children) {
      replaceMissingImages(child, filePath);
    }
  }
}

export default function remarkStripMissingImages() {
  return (tree, file) => {
    replaceMissingImages(tree, file?.path ? String(file.path) : '');
  };
}