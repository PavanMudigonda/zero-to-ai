/**
 * Playwright test: validate all navigation menu and home page links.
 *
 * Run against the live site:
 *   BASE_URL=https://zero-to-ai.dev node next-docs/test-nav-links.mjs
 *
 * Run against a local dev server (start with `npm run dev` first):
 *   node next-docs/test-nav-links.mjs
 */
import { chromium } from 'playwright';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';

async function testNavLinks() {
  console.log(`Testing navigation links on ${BASE_URL}…`);

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  // ── 1. Load home page ────────────────────────────────────────────────────
  console.log('\n[1/4] Loading home page…');
  await page.goto(BASE_URL, { waitUntil: 'domcontentloaded', timeout: 30_000 });

  // ── 2. Expand every collapsed sidebar section ─────────────────────────────
  console.log('[2/4] Expanding sidebar sections…');
  let expanded = true;
  let passes = 0;
  while (expanded && passes < 30) {
    expanded = false;
    passes++;
    const buttons = await page.$$('button[aria-expanded="false"]');
    for (const btn of buttons) {
      try {
        const box = await btn.boundingBox();
        if (box) {
          await btn.click({ timeout: 2_000 });
          expanded = true;
          await page.waitForTimeout(150);
        }
      } catch (_) {
        // ignore stale/hidden buttons
      }
    }
  }

  // ── 3. Collect links ──────────────────────────────────────────────────────
  console.log('[3/4] Collecting links from sidebar and home page…');

  const origin = new URL(BASE_URL).origin;

  const links = await page.evaluate((origin) => {
    const seen = new Set();
    const results = [];

    function collect(root, label) {
      for (const a of root.querySelectorAll('a[href]')) {
        const href = a.href;
        if (!href.startsWith(origin)) continue;
        const url = new URL(href);
        if (url.hash) continue;                 // skip same-page anchors
        if (seen.has(url.pathname)) continue;
        seen.add(url.pathname);
        results.push({
          text: (a.innerText || a.textContent || '').trim().slice(0, 80),
          href,
          source: label,
        });
      }
    }

    const sidebar = document.querySelector('aside, nav[aria-label], [class*="sidebar"]');
    if (sidebar) collect(sidebar, 'sidebar');

    const main = document.querySelector('main, article');
    if (main) collect(main, 'main');

    // fall back to whole body if nothing found
    if (results.length === 0) collect(document.body, 'body');

    return results;
  }, origin);

  if (links.length === 0) {
    console.error('ERROR: No internal links found on the home page.');
    await browser.close();
    process.exit(1);
  }

  console.log(`   Found ${links.length} unique internal links to test.`);

  // ── 4. Visit every link ───────────────────────────────────────────────────
  console.log('[4/4] Checking each link…\n');

  const broken = [];

  for (const [i, link] of links.entries()) {
    const label = `(${i + 1}/${links.length}) [${link.source}] "${link.text}" → ${link.href}`;
    try {
      const response = await page.goto(link.href, {
        waitUntil: 'domcontentloaded',
        timeout: 20_000,
      });

      const status   = response?.status() ?? 0;
      const pageTitle = await page.title();
      const is404    = status === 404
        || pageTitle.toLowerCase().includes('404')
        || pageTitle.toLowerCase().includes('not found');
      const isError  = status >= 400;

      if (is404 || isError) {
        console.error(`  ✗ BROKEN  ${label}  (HTTP ${status})`);
        broken.push({ ...link, status });
      } else {
        console.log(`  ✓ OK      ${label}`);
      }
    } catch (err) {
      console.error(`  ✗ ERROR   ${label}  (${err.message})`);
      broken.push({ ...link, error: err.message });
    }
  }

  // ── Summary ───────────────────────────────────────────────────────────────
  console.log('\n══════════════ RESULTS ══════════════');
  console.log(`Tested : ${links.length} links`);
  console.log(`Broken : ${broken.length} links`);

  if (broken.length > 0) {
    console.log('\nBroken links:');
    broken.forEach((l) =>
      console.log(`  • [${l.source}] "${l.text}" → ${l.href}  (${l.status ?? l.error})`),
    );
  }

  await browser.close();

  if (broken.length > 0) {
    process.exit(1);
  } else {
    console.log('\n✅ All navigation and home page links are working!');
  }
}

testNavLinks().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
