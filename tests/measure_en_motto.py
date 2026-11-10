import asyncio
import os
from playwright.async_api import async_playwright

async def measure_en():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        await page.evaluate('applyLanguage("en")')
        brand_w = await page.evaluate('''() => {
            const el = document.querySelector(".hero-brand-name");
            const range = document.createRange();
            range.selectNodeContents(el);
            return range.getBoundingClientRect().width;
        }''')
        print(f"English Brand width: {brand_w:.1f}px")
        for s in [1.5, 1.55, 1.58, 1.6, 1.63, 1.65]:
            await page.evaluate(f'''() => {{
                document.querySelector(".hero-motto").style.setProperty("font-size", "{s}rem", "important");
            }}''')
            m_w = await page.evaluate('''() => {
                const el = document.querySelector(".hero-motto");
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }''')
            print(f"s={s}rem -> Motto width: {m_w:.1f}px (diff: {m_w - brand_w:+.1f}px)")
        await browser.close()

asyncio.run(measure_en())
