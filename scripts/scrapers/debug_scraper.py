import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://codelabs.developers.google.com/?category=aiandmachinelearning")
        await page.wait_for_timeout(3000)
        content = await page.content()
        with open("codelabs_source.html", "w") as f:
            f.write(content)
        await browser.close()

asyncio.run(run())
