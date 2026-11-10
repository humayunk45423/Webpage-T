import asyncio
import os
from playwright.async_api import async_playwright

async def preview_chips():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        # Apply chip-4 removal and chip-2 centering
        css = """
        .chip-4 { display: none !important; }
        .chip-2 {
            top: 50% !important;
            transform: translateY(-50%) !important;
            right: 0% !important;
        }
        """
        await page.add_style_tag(content=css)
        for lang in ['bn', 'en']:
            await page.evaluate(f'applyLanguage("{lang}")')
            for theme in ['dark', 'light']:
                await page.evaluate(f'applyTheme("{theme}")')
                await page.wait_for_timeout(100)
                await page.locator('.hero-phone-stage').screenshot(path=f"tests/preview_stage_chips_{theme}_{lang}.png")
                
        # Also desktop
        dpage = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await dpage.goto(url)
        css_desk = """
        .chip-4 { display: none !important; }
        .chip-2 {
            top: 50% !important;
            transform: translateY(-50%) !important;
            right: -6% !important;
        }
        """
        await dpage.add_style_tag(content=css_desk)
        for lang in ['bn', 'en']:
            await dpage.evaluate(f'applyLanguage("{lang}")')
            await dpage.wait_for_timeout(100)
            await dpage.locator('.hero-phone-stage').screenshot(path=f"tests/preview_desk_stage_{lang}.png")
            
        await dpage.close()
        await page.close()
        await browser.close()
        print("Captured chips preview successfully!")

asyncio.run(preview_chips())

