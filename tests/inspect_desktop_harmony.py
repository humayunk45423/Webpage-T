import asyncio
import os
from playwright.async_api import async_playwright

async def inspect():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        for lang in ['en', 'bn']:
            await page.evaluate(f'applyLanguage("{lang}")')
            await page.wait_for_timeout(200)
            await page.locator('#hero').screenshot(path=f'tests/desktop_{lang}_inspect.png')
            
            items = ['.hero-badges-cluster', '.hero-title', '.hero-brand-name', '.hero-motto', '.hero-desc', '.hero-actions', '.hero-stats-row']
            print(f'=== DESKTOP {lang.upper()} ===')
            for sel in items:
                el = page.locator(sel)
                box = await el.bounding_box()
                style = await page.evaluate(f'''() => {{
                    const s = getComputedStyle(document.querySelector("{sel}"));
                    return {{
                        fontSize: s.fontSize,
                        lineHeight: s.lineHeight,
                        marginBottom: s.marginBottom,
                        letterSpacing: s.letterSpacing,
                        fontFamily: s.fontFamily
                    }};
                }}''')
                print(f'{sel}:\n  box={box}\n  style={style}')
        await browser.close()

asyncio.run(inspect())

