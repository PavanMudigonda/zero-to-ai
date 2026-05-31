const { chromium } = require('playwright');

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';
const SEED_PATH = normalizePath(process.env.SEED_PATH || '/15-ai-agents/01_START_HERE');
const VIEWPORT = { width: 1440, height: 1600 };

function normalizeText(value) {
  return (value || '').replace(/\s+/g, ' ').trim();
}

function normalizePath(value) {
  const pathname = new URL(value, BASE_URL).pathname;
  return pathname === '/' ? pathname : pathname.replace(/\/+$/, '');
}

async function waitForPageToSettle(page) {
  await page.waitForLoadState('domcontentloaded');
  await page.locator('body').waitFor({ state: 'visible', timeout: 30_000 });
  await page.waitForTimeout(400);
}

async function openPage(page, path) {
  const response = await page.goto(new URL(path, BASE_URL).toString(), {
    waitUntil: 'domcontentloaded',
    timeout: 30_000,
  });

  await waitForPageToSettle(page);
  return response;
}

async function getSidebar(page) {
  const sidebar = page.locator('aside.nextra-sidebar').first();
  await sidebar.waitFor({ state: 'visible', timeout: 15_000 });
  return sidebar;
}

async function collectTopLevelSectionPaths(page) {
  const sidebar = await getSidebar(page);

  return sidebar.evaluate((node) => {
    const normalizePathname = (value) => (value === '/' ? value : value.replace(/\/+$/, ''));
    const isVisible = (element) => {
      const style = window.getComputedStyle(element);
      return (
        style.display !== 'none' &&
        style.visibility !== 'hidden' &&
        !element.closest('[hidden]') &&
        Boolean(element.offsetWidth || element.offsetHeight || element.getClientRects().length)
      );
    };

    const seen = new Set();
    const paths = [];
    const rootList = node.querySelector('ul');

    if (!rootList) {
      return paths;
    }

    for (const item of rootList.querySelectorAll(':scope > li')) {
      const control = item.querySelector(':scope > a[href], :scope > button[data-href]');
      const href = control?.getAttribute('href') || control?.getAttribute('data-href');

      if (!control || !href || !href.startsWith('/') || href === '/' || !isVisible(control)) {
        continue;
      }

      const path = normalizePathname(href);
      if (seen.has(path)) {
        continue;
      }

      seen.add(path);
      paths.push(path);
    }

    return paths;
  });
}

async function getSectionRootItem(sidebar, sectionPath) {
  const rootItem = sidebar
    .locator(`li:has(> button[data-href="${sectionPath}"]), li:has(> a[href="${sectionPath}"])`)
    .first();

  if ((await rootItem.count()) === 0) {
    throw new Error(`Could not find sidebar section for ${sectionPath}`);
  }

  await rootItem.waitFor({ state: 'visible', timeout: 15_000 });
  return rootItem;
}

async function expandSidebarSection(page, sectionPath) {
  const sidebar = await getSidebar(page);
  const rootItem = await getSectionRootItem(sidebar, sectionPath);
  const rootButton = rootItem.locator(`:scope > button[data-href="${sectionPath}"]`).first();
  const rootLink = rootItem.locator(`:scope > a[href="${sectionPath}"]`).first();

  if ((await rootButton.count()) === 0) {
    if ((await rootLink.count()) === 0) {
      throw new Error(`Sidebar section for ${sectionPath} has no clickable root control`);
    }

    await rootLink.waitFor({ state: 'visible', timeout: 15_000 });
    return rootItem;
  }

  const isRootOpen = await rootButton.evaluate((button) => button.closest('li')?.classList.contains('open'));

  if (!isRootOpen) {
    await rootButton.scrollIntoViewIfNeeded();
    await rootButton.click();
    await page.waitForTimeout(200);
  }

  for (let pass = 0; pass < 50; pass += 1) {
    const nextClosedPath = await rootItem.evaluate((item, currentSectionPath) => {
      const nextClosedButton = Array.from(item.querySelectorAll('button[data-href]')).find((button) => {
        if (button.getAttribute('data-href') === currentSectionPath) {
          return false;
        }

        const listItem = button.closest('li');
        const childList = listItem?.querySelector(':scope > div > ul');
        const isVisible = Boolean(button.offsetWidth || button.offsetHeight || button.getClientRects().length);
        return isVisible && Boolean(childList?.querySelector(':scope > li')) && !listItem.classList.contains('open');
      });

      return nextClosedButton?.getAttribute('data-href') || null;
    }, sectionPath);

    if (!nextClosedPath) {
      return rootItem;
    }

    const nextButton = rootItem.locator(`button[data-href="${nextClosedPath}"]`).first();
    await nextButton.scrollIntoViewIfNeeded();
    await nextButton.click();
    await page.waitForTimeout(150);
  }

  throw new Error(`Sidebar section ${sectionPath} did not finish expanding`);
}

async function collectVisibleInternalLinks(rootItem) {
  return rootItem.evaluate((item, baseUrl) => {
    const origin = new URL(baseUrl).origin;
    const seen = new Set();
    const links = [];
    const normalize = (value) => (value || '').replace(/\s+/g, ' ').trim();
    const normalizePathname = (value) => (value === '/' ? value : value.replace(/\/+$/, ''));

    for (const anchor of item.querySelectorAll('a[href]')) {
      const href = anchor.getAttribute('href');
      const text = normalize(anchor.textContent);

      if (!href || !text) {
        continue;
      }

      const url = new URL(href, origin);
      const style = window.getComputedStyle(anchor);
      const isVisible =
        style.display !== 'none' &&
        style.visibility !== 'hidden' &&
        !anchor.closest('[hidden]') &&
        Boolean(anchor.offsetWidth || anchor.offsetHeight || anchor.getClientRects().length);

      if (!isVisible || url.origin !== origin || url.hash) {
        continue;
      }

      const path = normalizePathname(url.pathname);
      if (seen.has(path)) {
        continue;
      }

      seen.add(path);
      links.push({ text, path });
    }

    return links;
  }, BASE_URL);
}

async function assertNoSelfNestedCurrentPage(rootItem, currentPath) {
  const issue = await rootItem.evaluate((item, startPath) => {
    const normalize = (value) => (value || '').replace(/\s+/g, ' ').trim();
    const normalizePathname = (value) => (value === '/' ? value : value.replace(/\/+$/, ''));
    const isVisible = (element) => {
      const style = window.getComputedStyle(element);
      return (
        style.display !== 'none' &&
        style.visibility !== 'hidden' &&
        !element.closest('[hidden]') &&
        Boolean(element.offsetWidth || element.offsetHeight || element.getClientRects().length)
      );
    };

    const currentLink = Array.from(item.querySelectorAll('a[href]')).find((anchor) => {
      if (!isVisible(anchor)) {
        return false;
      }

      const path = normalizePathname(new URL(anchor.getAttribute('href'), window.location.origin).pathname);
      return path === startPath;
    });

    if (!currentLink) {
      return {
        kind: 'missing-current-link',
        startPath,
      };
    }

    const currentText = normalize(currentLink.textContent);
    let parentList = currentLink.closest('ul');

    while (parentList) {
      const parentItem = parentList.closest('li');
      if (!parentItem) {
        break;
      }

      const parentButton = parentItem.querySelector(':scope > button');
      const parentText = normalize(parentButton?.textContent);

      if (parentText && parentText.toLowerCase() === currentText.toLowerCase()) {
        return {
          kind: 'self-nested-current-page',
          label: currentText,
        };
      }

      parentList = parentItem.parentElement?.closest('ul') || null;
    }

    return null;
  }, currentPath);

  if (!issue) {
    return;
  }

  if (issue.kind === 'missing-current-link') {
    throw new Error(`Sidebar does not show the current page link for ${issue.startPath}`);
  }

  throw new Error(
    `Malformed sidebar nesting: current page "${issue.label}" appears nested under another visible "${issue.label}" sidebar item`,
  );
}

async function assertHealthyPage(page, response, expectedPath, pageErrors) {
  const status = response?.status() ?? 0;

  const diagnostics = await page.evaluate(() => {
    const bodyText = document.body.innerText.toLowerCase();
    const title = document.title.toLowerCase();

    return {
      currentPath: window.location.pathname,
      has404:
        title.includes('404') ||
        title.includes('not found') ||
        bodyText.includes('404: this page could not be found') ||
        bodyText.includes('this page could not be found'),
      hasAppError:
        bodyText.includes('application error') ||
        bodyText.includes('something went wrong') ||
        Boolean(document.querySelector('body[data-nextjs-error="true"]')),
    };
  });

  if (status >= 400) {
    throw new Error(`HTTP ${status} on ${expectedPath}`);
  }

  if (normalizePath(diagnostics.currentPath) !== expectedPath) {
    throw new Error(`Expected ${expectedPath} but landed on ${diagnostics.currentPath}`);
  }

  if (diagnostics.has404) {
    throw new Error(`404/not found UI detected on ${expectedPath}`);
  }

  if (diagnostics.hasAppError) {
    throw new Error(`Application error UI detected on ${expectedPath}`);
  }

  if (pageErrors.length > 0) {
    throw new Error(`Unhandled page errors on ${expectedPath}: ${pageErrors.join(' | ')}`);
  }
}

async function runSectionCheck(page, sectionPath, pageErrors) {
  const failures = [];
  const startResponse = await openPage(page, sectionPath);

  if (!startResponse || !startResponse.ok()) {
    const status = startResponse ? startResponse.status() : 'NO_RESPONSE';
    throw new Error(`Unable to load start page ${new URL(sectionPath, BASE_URL).toString()} (${status})`);
  }

  const rootItem = await expandSidebarSection(page, sectionPath);
  const links = await collectVisibleInternalLinks(rootItem);

  if (links.length === 0) {
    throw new Error(`No visible internal sidebar links found under ${sectionPath}`);
  }

  try {
    await assertNoSelfNestedCurrentPage(rootItem, sectionPath);
  } catch (error) {
    failures.push(`Initial sidebar state: ${normalizeText(error.message)}`);
  }

  for (const link of links) {
    try {
      pageErrors.length = 0;
      const response = await openPage(page, link.path);
      await assertHealthyPage(page, response, link.path, pageErrors);
      const currentRootItem = await expandSidebarSection(page, sectionPath);
      await assertNoSelfNestedCurrentPage(currentRootItem, link.path);
    } catch (error) {
      failures.push(`${link.path}: ${normalizeText(error.message)}`);
    }
  }

  return { links, failures };
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: VIEWPORT });
  const page = await context.newPage();
  const pageErrors = [];

  page.on('pageerror', (error) => {
    pageErrors.push(normalizeText(error.message));
  });

  try {
    console.log(`Testing all left sidebar sections on ${BASE_URL}`);
    await openPage(page, SEED_PATH);

    const sectionPaths = await collectTopLevelSectionPaths(page);

    if (sectionPaths.length === 0) {
      throw new Error('Could not discover any top-level sidebar sections');
    }

    const failures = [];

    for (const sectionPath of sectionPaths) {
      try {
        const result = await runSectionCheck(page, sectionPath, pageErrors);

        if (result.failures.length > 0) {
          console.error(`\nSection failures for ${sectionPath}:`);
          result.failures.forEach((failure) => console.error(`- ${failure}`));
          failures.push(...result.failures.map((failure) => `${sectionPath}: ${failure}`));
          continue;
        }

        console.log(`PASS ${sectionPath} (${result.links.length} links)`);
      } catch (error) {
        const failure = `${sectionPath}: ${normalizeText(error.message)}`;
        failures.push(failure);
        console.error(`FAIL ${failure}`);
      }
    }

    if (failures.length > 0) {
      console.error(`\nFound ${failures.length} sidebar navigation failures.`);
      process.exitCode = 1;
      return;
    }

    console.log('\nAll left sidebar sections loaded successfully.');
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(normalizeText(error.stack || error.message));
  process.exit(1);
});