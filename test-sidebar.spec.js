const { chromium } = require('playwright');
const http = require('http');

(async () => {
    console.log('Launching browser...');
    const browser = await chromium.launch({ headless: true });
    try {
        const page = await browser.newPage();
        console.log('Navigating to http://localhost:3000...');
        await page.goto('http://localhost:3000', { waitUntil: 'load' });
        
        console.log('Expanding sidebar...');
        let newlyExpanded = true;
        let maxLoops = 20;
        while (newlyExpanded && maxLoops > 0) {
            newlyExpanded = false;
            maxLoops--;
            const buttons = await page.$$('button[aria-expanded="false"]');
            for (const btn of buttons) {
                try {
                    const bBox = await btn.boundingBox();
                    if (bBox && bBox.height > 0) {
                        await btn.click({ timeout: 500 });
                        newlyExpanded = true;
                    }
                } catch(e) {}
            }
            await page.waitForTimeout(200);
        }
        
        console.log('Fetching all links in sidebar...');
        const links = await page.evaluate(() => {
            const sidebar = document.querySelector('aside') || document.querySelector('nav') || document.body;
            let aTags = Array.from(sidebar.querySelectorAll('a'));
            return aTags.map(a => ({
                text: a.innerText.trim(),
                href: a.href
            })).filter(l => l.text && l.href && l.href.startsWith(window.location.origin) && !l.href.includes('#'));
        });
        
        const uniqueLinks = [];
        const seen = new Set();
        for (const l of links) {
            if (!seen.has(l.href)) {
                seen.add(l.href);
                uniqueLinks.push(l);
            }
        }
        
        console.log(`Checking ${uniqueLinks.length} unique sidebar links for naming conventions...`);
        let errors = [];
        let seq = 1;
        
        for (const link of uniqueLinks) {
            // Validate prefix (starts with a number)
            const prefixMatch = link.text.match(/^(\d+)[\-\.\s_]?/);
            if (!prefixMatch) {
                // Ignore empty links or maybe known non-numbered ones, but per user request: "every single link prefix with number if its missing"
                errors.push(`Missing number prefix: "${link.text}" -> ${link.href.split('3000')[1]}`);
            } else {
                const linkNum = parseInt(prefixMatch[1], 10);
                if (linkNum < seq - 10) { 
                    seq = linkNum; 
                } else if (linkNum > seq + 10) {
                     errors.push(`Out of sequence: "${link.text}" (expected something close to ${seq})`);
                }
                seq = linkNum + 1;
            }
        }

        console.log('Link errors found:', errors.length);
        if (errors.length > 0) {
            console.log(errors.slice(0, 50).join('\n') + (errors.length > 50 ? '\n...and more' : ''));
        }

        console.log('\nValidating HTTP Statuses (Parallel Fetch)...');
        
        const maxConcurrent = 100;
        let active = 0;
        let index = 0;
        let loadErrors = [];
        
        await new Promise((resolve) => {
            const next = () => {
                if (index >= uniqueLinks.length && active === 0) {
                    resolve();
                    return;
                }
                while (active < maxConcurrent && index < uniqueLinks.length) {
                    const idx = index++;
                    active++;
                    const url = uniqueLinks[idx].href;
                    
                    http.get(url, (res) => {
                        let data = '';
                        res.on('data', chunk => data += chunk);
                        res.on('end', () => {
                            if (res.statusCode !== 200 || data.includes('404: This page could not be found')) {
                                loadErrors.push(`Failed [${res.statusCode}]: ${url}`);
                            }
                            active--;
                            next();
                        });
                    }).on('error', (err) => {
                        loadErrors.push(`Error on ${url}: ${err.message}`);
                        active--;
                        next();
                    });
                }
            };
            next();
        });

        console.log(`\nHTTP Check completed. Load errors: ${loadErrors.length}`);
        if (loadErrors.length > 0) {
            console.log(loadErrors.slice(0, 20).join('\n') + (loadErrors.length > 20 ? '\n...and more' : ''));
        }

        if (errors.length > 0 || loadErrors.length > 0) {
            console.error('\n--- TESTS COMPLETED WITH FAILURES ---');
            process.exit(1);
        } else {
            console.log('\nAll links tested successfully.');
            process.exit(0);
        }

    } catch (err) {
        console.error('Fatal error:', err);
    } finally {
        await browser.close();
    }
})();
