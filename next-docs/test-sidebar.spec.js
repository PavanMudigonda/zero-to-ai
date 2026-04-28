const { chromium } = require('playwright');

(async () => {
    console.log('Launching browser...');
    const browser = await chromium.launch({ headless: true });
    try {
        const page = await browser.newPage();
        console.log('Navigating to http://localhost:3000...');
        await page.goto('http://localhost:3000');
        
        console.log('Starting recursive expansion of sidebar...');
        
        // Nextra uses buttons with svgs to expand. Often they have specific classes or aria-expanded.
        // We'll repeatedly click any unexpanded collapse toggles until there are no more.
        let expanded = true;
        while (expanded) {
            expanded = false;
            // Trying to find buttons that look like expandtoggles and are not expanded
            const expandButtons = await page.$$('button[aria-expanded="false"], a[aria-expanded="false"] button');
            for (const btn of expandButtons) {
                const bBox = await btn.boundingBox();
                if (bBox) {
                    try {
                        await btn.click({ timeout: 1000 });
                        expanded = true;
                        await page.waitForTimeout(200); // let animation finish
                    } catch(e) {}
                }
            }
        }
        
        console.log('Fetching all links in sidebar...');
        // Assume nextra sidebar items are within an <nav> or aside.
        // Nextra typically uses an aside or nav element for the sidebar.
        // Let's just find all 'a' tags inside the standard nextra sidebar container or a common class like "x:sidebar"
        // Let's get links from an aside tag if present.
        const links = await page.evaluate(() => {
            const sidebar = document.querySelector('aside') || document.body;
            return Array.from(sidebar.querySelectorAll('a')).map(a => ({
                text: a.innerText.trim(),
                href: a.href
            })).filter(l => l.text && l.href && l.href.startsWith(window.location.origin) && !l.href.includes('#'));
        });
        
        console.log(`Found ${links.length} sidebar links.`);
        
        // De-duplicate
        const uniqueLinks = Array.from(new Map(links.map(l => [l.href, l])).values());
        console.log(`Testing ${uniqueLinks.length} unique sidebar links for sequence and errors...`);
        
        let errors = [];
        let previousValidNumber = null;
        
        for (const [index, link] of uniqueLinks.entries()) {
            console.log(`[${index+1}/${uniqueLinks.length}] Checking link: "${link.text}" -> ${link.href}`);
            
            // Check prefix and sequence
            // Assuming prefix looks like "00-", "1 ", "01-", etc.
            const match = link.text.match(/^(\d+)[\-\. ]/);
            if (!match) {
                errors.push(`"${link.text}" does not have a number prefix`);
            } else {
                const num = parseInt(match[1], 10);
                if (previousValidNumber !== null) {
                    if (num < previousValidNumber) {
                        errors.push(`Out of sequence: "${link.text}" (Seq ${num}) came after a link with Seq ${previousValidNumber}`);
                    }
                }
                previousValidNumber = num;
            }
            
            // Try to visit the link and see if it loads successfully (no Next.js error overlay)
            try {
                const navResponse = await page.goto(link.href, { waitUntil: 'load', timeout: 5000 });
                if (!navResponse.ok()) {
                    errors.push(`HTTP ${navResponse.status()} when loading ${link.href}`);
                    continue;
                }
                
                // Check if page contains Next.js error
                const errorDiv = await page.$('body[data-nextjs-error="true"]');
                if (errorDiv || await page.title() === '404: This page could not be found' || await page.evaluate(() => document.documentElement.innerHTML.includes('Application error:'))) {
                     errors.push(`Application or 404 error string found on ${link.href}`);
                }
            } catch (err) {
                errors.push(`Navigation failed or timeout for ${link.href}: ${err.message}`);
            }
        }
        
        if (errors.length > 0) {
            console.error('\n--- TESTS FAILED ---');
            errors.forEach(e => console.error('- ' + e));
            process.exit(1);
        } else {
            console.log('\nAll links tested successfully, are prefixed correctly, and load without error.');
        }

    } catch (err) {
        console.error('Script Failed:', err);
    } finally {
        await browser.close();
    }
})();
