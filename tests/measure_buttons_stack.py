import asyncio
import os
from playwright.async_api import async_playwright

async def measure_buttons():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        for w in [1024, 1200, 1280, 1366, 1440]:
            await page.set_viewport_size({'width': w, 'height': 800})
            for lang in ['en', 'bn']:
                await page.evaluate(f'applyLanguage("{lang}")')
                await page.wait_for_timeout(50)
                
                b1 = await page.locator('.hero-actions .btn-primary').bounding_box()
                b2 = await page.locator('.hero-actions .btn-secondary').bounding_box()
                container = await page.locator('.hero-actions').bounding_box()
                
                # Check if stacked (b2 y > b1 y + 10)
                is_stacked = b2['y'] > b1['y'] + 10
                print(f"Viewport {w}px | {lang.upper()}: b1_w={b1['width']:.1f}px, b2_w={b2['width']:.1f}px, total={b1['width']+b2['width']+14:.1f}px, container_w={container['width']:.1f}px, STACKED={is_stacked}")
                
        await browser.close()

asyncio.run(measure_buttons())

