import asyncio
import os
from playwright.async_api import async_playwright

async def measure():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for vp_w in [390, 360, 412]:
            page = await browser.new_page(viewport={'width': vp_w, 'height': 800})
            url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
            await page.goto(url)
            for lang in ['bn', 'en']:
                await page.evaluate(f'applyLanguage("{lang}")')
                await page.wait_for_timeout(100)
                badge_box = await page.locator('.apple-specialist-badge').bounding_box()
                
                # Get the actual text width (inline measurement) of hero-brand-name
                brand_w = await page.evaluate("""() => {
                    const el = document.querySelector('.hero-brand-name');
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    return range.getBoundingClientRect().width;
                }""")
                motto_w = await page.evaluate("""() => {
                    const el = document.querySelector('.hero-motto');
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    return range.getBoundingClientRect().width;
                }""")
                print(f"VP {vp_w} | {lang}: Badge width = {badge_box['width']:.1f}px, Brand text width = {brand_w:.1f}px, Motto text width = {motto_w:.1f}px")
            await page.close()
        await browser.close()

asyncio.run(measure())

