import asyncio
import os
from playwright.async_api import async_playwright

async def preview_visuals():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        # Test styling:
        # brand-name sized to match the badge
        # motto kept comfortable and harmonious
        css = """
        .hero-brand-name {
            font-size: clamp(2.15rem, 9.9vw, 2.45rem) !important;
            letter-spacing: -0.025em;
            line-height: 1.15 !important;
            margin-bottom: 2px !important;
        }
        .hero-motto {
            font-size: clamp(1.68rem, 7.2vw, 2.12rem) !important;
            letter-spacing: -0.02em;
            line-height: 1.24 !important;
        }
        """
        await page.add_style_tag(content=css)
        
        for lang in ['bn', 'en']:
            await page.evaluate(f'applyLanguage("{lang}")')
            for theme in ['light', 'dark']:
                await page.evaluate(f'applyTheme("{theme}")')
                await page.wait_for_timeout(150)
                await page.locator('#hero').screenshot(path=f"tests/preview_brand_match_{theme}_{lang}.png")
                print(f"Captured: preview_brand_match_{theme}_{lang}.png")
                
        await browser.close()

asyncio.run(preview_visuals())

