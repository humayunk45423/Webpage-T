import asyncio
import os
from playwright.async_api import async_playwright

async def inspect_viewports():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # Test candidate clamp for brand name: clamp(1.9rem, 7.8vw, 2.45rem)
        css_inject = """
        .hero-brand-name {
            font-size: clamp(1.85rem, 7.5vw, 2.42rem) !important;
            letter-spacing: -0.02em;
        }
        """
        
        for w in [360, 375, 390, 412]:
            page = await browser.new_page(viewport={'width': w, 'height': 800})
            url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
            await page.goto(url)
            await page.add_style_tag(content=css_inject)
            
            for lang in ['bn', 'en']:
                await page.evaluate(f'applyLanguage("{lang}")')
                await page.wait_for_timeout(100)
                
                badge_w = await page.evaluate("() => document.querySelector('.apple-specialist-badge').getBoundingClientRect().width")
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
                scroll_w = await page.evaluate("() => document.documentElement.scrollWidth")
                client_w = await page.evaluate("() => document.documentElement.clientWidth")
                overflow = scroll_w > client_w
                
                print(f"Viewport {w}px | {lang.upper()}: Badge = {badge_w:.1f}px, Brand = {brand_w:.1f}px ({brand_w/badge_w*100:.1f}%), Motto = {motto_w:.1f}px, Overflow = {overflow}")
                
            # Screenshot hero on 390px
            if w == 390:
                for lang in ['bn', 'en']:
                    await page.evaluate(f'applyLanguage("{lang}")')
                    await page.wait_for_timeout(100)
                    await page.locator('#hero').screenshot(path=f"tests/preview_brand_bigger_{lang}.png")
            await page.close()
            
        await browser.close()

asyncio.run(inspect_viewports())

