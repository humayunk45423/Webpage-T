import asyncio
import os
from playwright.async_api import async_playwright

async def test_length_similarity():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        css = """
        .hero-brand-name {
            font-size: clamp(2.15rem, 10.0vw, 2.50rem) !important;
            letter-spacing: -0.025em;
            line-height: 1.22 !important;
            margin-bottom: 2px !important;
            padding: 6px 2px 5px !important;
            white-space: nowrap !important;
        }
        
        /* English Motto */
        .hero-motto {
            font-size: clamp(1.50rem, 6.4vw, 2.05rem) !important;
            letter-spacing: -0.02em;
            line-height: 1.26 !important;
            padding: 4px 2px 6px !important;
            white-space: nowrap !important;
        }
        
        /* Bengali Motto: Exact same collective length as মোবাইল এক্সপ্রেস */
        .lang-bn .hero-motto {
            font-size: clamp(1.72rem, 8.0vw, 2.05rem) !important;
            letter-spacing: 0 !important;
            line-height: 1.28 !important;
            padding: 4px 2px 6px !important;
            white-space: nowrap !important;
        }
        """
        
        for w in [320, 360, 375, 390, 412, 430]:
            page = await browser.new_page(viewport={'width': w, 'height': 800})
            await page.goto(url)
            await page.add_style_tag(content=css)
            
            for lang in ['bn', 'en']:
                await page.evaluate(f'applyLanguage("{lang}")')
                await page.wait_for_timeout(50)
                
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
                diff = abs(brand_w - motto_w)
                print(f"w={w}px | {lang.upper()}: Brand = {brand_w:.1f}px, Motto = {motto_w:.1f}px, Diff = {diff:.1f}px (match: {min(brand_w,motto_w)/max(brand_w,motto_w)*100:.1f}%), Overflow={scroll_w > client_w}")
                
            if w == 390:
                for lang in ['bn', 'en']:
                    await page.evaluate(f'applyLanguage("{lang}")')
                    await page.locator('.hero-title').screenshot(path=f"tests/title_match_{lang}.png")
            await page.close()
            
        await browser.close()

asyncio.run(test_length_similarity())

