const puppeteer = require('puppeteer');

(async () => {
    const baseUrl = process.env.BASE_URL || 'http://localhost:3000';
    const routes = [
        '/33-roadmaps/01_overview',
        '/33-roadmaps/02_core_systems',
        '/33-roadmaps/03_advanced_topics',
        '/33-roadmaps/04_end_to_end_flows',
        '/15-ai-agents/01_START_HERE'
    ];

    console.log('Starting puppeteer tests...');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    let hasErrors = false;

    for (const route of routes) {
        const urlPath = `${route}${process.env.STATIC_EXPORT === 'true' ? '.html' : ''}`;
        const url = new URL(urlPath, baseUrl).href;
        console.log(`Processing: ${url}`);
        try {
            await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
            await new Promise(resolve => setTimeout(resolve, 5000));
            const result = await page.evaluate(() => {
                const diagrams = document.querySelectorAll(
                    'article .zoomable-mermaid-render svg, article .jk-mermaid-diagram svg'
                );
                const viewers = document.querySelectorAll('.zoomable-mermaid-render');
                const maximizeButtons = [...viewers].filter((container) =>
                    container.parentElement?.querySelector('button')?.textContent?.trim() === 'Maximize'
                );
                const rawMermaidBlocks = document.querySelectorAll('article code.language-mermaid');
                const notebookDiagrams = document.querySelectorAll('.jk-notebook-container .jk-mermaid-diagram');
                const errors = [...document.querySelectorAll('article [role="alert"]')]
                    .map((element) => element.textContent || 'Rendering error');

                for (const diagram of diagrams) {
                    if (diagram.textContent.includes('Syntax error')) {
                        errors.push('SVG contains a syntax error: ' + diagram.textContent.substring(0, 50));
                    }
                }

                return {
                    svgCount: diagrams.length,
                    viewerCount: viewers.length,
                    maximizeButtonCount: maximizeButtons.length,
                    rawMermaidBlocks: rawMermaidBlocks.length,
                    notebookDiagrams: notebookDiagrams.length,
                    errors
                };
            });

            console.log(`  -> Mermaid SVGs: ${result.svgCount} | Raw Mermaid blocks: ${result.rawMermaidBlocks}`);
            if (route.endsWith('/15-ai-agents/01_START_HERE')) {
                console.log(`  -> Notebook diagrams: ${result.notebookDiagrams}`);
                if (result.notebookDiagrams === 0) {
                    console.log('  -> ERROR: Notebook Mermaid block was not rendered');
                    hasErrors = true;
                    continue;
                }
            } else if (result.viewerCount === 0) {
                console.log('  -> ERROR: Mermaid diagrams are missing the zoom/full-screen viewer');
                hasErrors = true;
                continue;
            }
            if (result.svgCount === 0 || result.rawMermaidBlocks > 0) {
                console.log('  -> ERROR: Mermaid diagram missing or still displayed as code');
                hasErrors = true;
            } else if (result.errors.length > 0) {
                console.log(`  -> ERRORS DETECTED:`, result.errors);
                hasErrors = true;
            } else {
                if (route.startsWith('/33-roadmaps/')) {
                    if (result.maximizeButtonCount === 0) {
                        console.log('  -> ERROR: Full-screen control not found');
                        hasErrors = true;
                        continue;
                    }
                    await page.evaluate(() => {
                        const button = [...document.querySelectorAll('button')]
                            .find((element) => element.textContent?.trim() === 'Maximize');
                        button?.click();
                    });
                    await page.waitForSelector('[role="dialog"][aria-label="Mermaid diagram viewer"]', { timeout: 5000 });
                    const readZoomLevel = () => page.$eval('[role="dialog"] button[title="Zoom in (+)"]', (button) => {
                        const dialog = button.closest('[role="dialog"]');
                        return Number(dialog?.querySelector('span')?.textContent?.replace('%', ''));
                    });
                    const beforeZoom = await readZoomLevel();
                    await page.click('[role="dialog"] button[title="Zoom in (+)"]');
                    await new Promise(resolve => setTimeout(resolve, 300));
                    const zoomedIn = await readZoomLevel();
                    await page.click('[role="dialog"] button[title="Zoom out (−)"]');
                    await new Promise(resolve => setTimeout(resolve, 300));
                    const zoomedOut = await readZoomLevel();
                    await page.click('[role="dialog"] button[title="Close (Esc)"]');
                    if (!(zoomedIn > beforeZoom && zoomedOut < zoomedIn)) {
                        console.log('  -> ERROR: Zoom controls did not change the zoom level in both directions');
                        hasErrors = true;
                        continue;
                    }
                    console.log('  -> Full-screen and zoom controls: PASS');
                }
                console.log('  -> PASS');
            }
        } catch (e) {
            console.log(`  -> Exception on navigation: ${e.message}`);
            hasErrors = true;
        }
    }
    await browser.close();
    process.exit(hasErrors ? 1 : 0);
})();
