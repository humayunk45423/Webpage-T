import asyncio
import os
from playwright.async_api import async_playwright

async def test_sizes():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        for lang in ['bn', 'en']:
            await page.evaluate(f'applyLanguage("{lang}")')
            badge_w = await page.evaluate("() => document.querySelector('.apple-specialist-badge').getBoundingClientRect().width")
            print(f"\n--- {lang.upper()} (Badge width = {badge_w:.1f}px) ---")
            
            for fsize in [2.0, 2.2, 2.35, 2.4, 2.5, 2.6, 2.7, 2.8]:
                await page.evaluate(f"""() => {{
                    document.querySelector('.hero-brand-name').style.fontSize = '{fsize}rem';
                }}""")
                brand_w = await page.evaluate("""() => {
                    const el = document.querySelector('.hero-brand-name');
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    return range.getBoundingClientRect().width;
                }""")
                ratio = brand_w / badge_w
                print(f"fontSize = {fsize}rem -> Brand width = {brand_w:.1f}px ({ratio*100:.1f}% of badge)")
                
        await browser.close()

asyncio.run(test_sizes())

