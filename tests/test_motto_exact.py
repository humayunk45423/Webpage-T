import asyncio
import os
from playwright.async_api import async_playwright

async def inspect_motto_sizes():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page.goto(url)
        await page.evaluate('applyLanguage("bn")')
        brand_w = await page.evaluate("""() => {
            const el = document.querySelector('.hero-brand-name');
            const range = document.createRange();
            range.selectNodeContents(el);
            return range.getBoundingClientRect().width;
        }""")
        print(f"Target Brand Width in BN (390px): {brand_w:.1f}px")
        
        for fsize in [1.6, 1.7, 1.8, 1.85, 1.9, 1.95, 2.0, 2.05, 2.1, 2.15, 2.2]:
            await page.evaluate(f"""() => {{
                document.querySelector('.hero-motto').style.setProperty('font-size', '{fsize}rem', 'important');
            }}""")
            motto_w = await page.evaluate("""() => {
                const el = document.querySelector('.hero-motto');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            ratio = motto_w / brand_w * 100
            print(f"Motto fsize={fsize}rem -> width={motto_w:.1f}px ({ratio:.1f}% of brand, diff: {motto_w - brand_w:+.1f}px)")
            
        await page.close()
        await browser.close()

asyncio.run(inspect_motto_sizes())

