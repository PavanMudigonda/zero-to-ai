export function normalizeMermaidSource(source) {
  return source.replace(/\r\n?/g, '\n').trim();
}

export async function hashMermaidSource(source) {
  const normalizedSource = normalizeMermaidSource(source);
  const digest = await globalThis.crypto.subtle.digest(
    'SHA-256',
    new TextEncoder().encode(normalizedSource),
  );

  return [...new Uint8Array(digest)]
    .map((byte) => byte.toString(16).padStart(2, '0'))
    .join('');
}
