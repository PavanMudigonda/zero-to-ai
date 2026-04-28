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
            await page.goto(route, { waitUntil: 'networkidle0', timeout: 30000 });
            await new Promise(resolve => setTimeout(resolve, 5000));
            // Evaluate errors and svgs
            const result = await page.evaluate(() => {
                const containers = document.querySelectorAll('.zoomable-mermaid-render');
                let svgCount = 0;
                let errors = [];

                for (let i = 0; i < containers.length; i++) {
                    const c = containers[i];
                    const svg = c.querySelector('svg');
                    if (svg) {
                        svgCount++;
                        if (svg.textContent.includes('Syntax error')) {
                            errors.push('Syntax error in SVG ' + i + ': ' + svg.textContent.substring(0, 50));
                        }
                    } else {
                        errors.push('Container ' + i + ' missing SVG! InnerHTML: ' + c.innerHTML.substring(0, 100));
                    }
                }

                return { containers: containers.length, svgCount, errors };
            });

            console.log(`  -> Containers: ${result.containers} | SVGs inside: ${result.svgCount}`);
            if (result.errors.length > 0) {
                console.log(`  -> ERRORS DETECTED:`, result.errors);
                hasErrors = true;
            } else if (result.containers === 0) {
                console.log(`  -> WARNING: No containers found`);
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
