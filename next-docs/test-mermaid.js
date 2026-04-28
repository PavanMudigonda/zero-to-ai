const puppeteer = require('puppeteer');

(async () => {
    const routes = [
        'http://localhost:3000/33-roadmaps/01_overview',
        'http://localhost:3000/33-roadmaps/02_core_systems',
        'http://localhost:3000/33-roadmaps/03_advanced_topics',
        'http://localhost:3000/33-roadmaps/04_end_to_end_flows'
    ];

    console.log('Starting puppeteer tests...');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    let hasErrors = false;

    for (const route of routes) {
        console.log(`Processing: ${route}`);
        try {
            await page.goto(route, { waitUntil: 'load', timeout: 20000 });
            await new Promise(resolve => setTimeout(resolve, 3000));
            // Evaluate errors and svgs
            const result = await page.evaluate(() => {
                const svgs = document.querySelectorAll('svg');
                let mermaidCount = 0;
                let errors = [];

                for (const svg of svgs) {
                    if (svg.id && svg.id.startsWith('dmermaid-')) mermaidCount++;
                    if (svg.classList.contains('mermaid')) mermaidCount++;
                    if (svg.textContent && svg.textContent.includes('Syntax error')) {
                        errors.push('SVG contains syntax error: ' + svg.textContent.substring(0, 60));
                    }
                }
                
                const rawMermaids = document.querySelectorAll('.mermaid, .language-mermaid');
                const rawErrors = document.querySelectorAll('.mermaid-error');
                for (const node of rawErrors) {
                    errors.push('Found .mermaid-error tag: ' + node.textContent.substring(0, 100));
                }

                return { svgCount: svgs.length, mermaidCount, rawCodeBlocks: rawMermaids.length, errors };
            });

            console.log(`  -> SVGs: ${result.svgCount} (of which Mermaids: ${result.mermaidCount})`);
            if (result.errors.length > 0) {
                console.log(`  -> ERRORS DETECTED:`, result.errors);
                hasErrors = true;
            } else if (result.mermaidCount === 0 && result.rawCodeBlocks > 0) {
                console.log(`  -> WARNING: No Mermaid SVGs found, but raw block exists (Count: ${result.rawCodeBlocks})`);
            } else {
                console.log(`  -> PASS`);
            }
        } catch (e) {
            console.log(`  -> Exception on navigation: ${e.message}`);
            hasErrors = true;
        }
    }
    await browser.close();
    process.exit(hasErrors ? 1 : 0);
})();
