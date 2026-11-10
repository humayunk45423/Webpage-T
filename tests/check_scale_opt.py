import asyncio
import os
from playwright.async_api import async_playwright

async def check_scale():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        css = """
        .hero-title {
            padding: 2px 0 !important;
            margin-bottom: 12px !important;
        }
        .hero-brand-name {
            font-size: clamp(2.15rem, 10.0vw, 2.50rem) !important;
            letter-spacing: -0.025em;
            line-height: 1.15 !important;
            margin-bottom: 3px !important;
            padding: 1px 0 !important;
            white-space: nowrap !important;
        }
        .hero-motto {
            font-size: clamp(1.50rem, 6.4vw, 2.05rem) !important;
            letter-spacing: -0.02em;
            line-height: 1.24 !important;
            padding: 2px 2px 4px !important;
            white-space: nowrap !important;
        }
        """
        
        for w in [320, 360, 390, 412]:
            page = await browser.new_page(viewport={'width': w, 'height': 800})
            url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
            await page.goto(url)
            await page.add_style_tag(content=css)
            
            for lang in ['bn', 'en']:
                await page.evaluate(f'applyLanguage("{lang}")')
                await page.wait_for_timeout(50)
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
                print(f"w={w} {lang}: Badge={badge_w:.1f}px, Brand={brand_w:.1f}px (diff: {brand_w - badge_w:+.1f}px), Motto={motto_w:.1f}px, Overflow={scroll_w > client_w}")
            await page.close()
            
        await browser.close()

asyncio.run(check_scale())

