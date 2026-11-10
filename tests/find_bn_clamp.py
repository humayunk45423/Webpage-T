import asyncio
import os
from playwright.async_api import async_playwright

async def find_bn_perfect_clamp():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        candidates = [
            "clamp(1.65rem, 7.4vw, 1.90rem)",
            "clamp(1.68rem, 7.5vw, 1.92rem)",
            "clamp(1.70rem, 7.6vw, 1.94rem)",
            "clamp(1.72rem, 7.7vw, 1.95rem)"
        ]
        
        for cand in candidates:
            css = f"""
            .hero-brand-name {{
                font-size: clamp(2.15rem, 10.0vw, 2.50rem) !important;
            }}
            .lang-bn .hero-motto {{
                font-size: {cand} !important;
                letter-spacing: 0 !important;
            }}
            """
            print(f"\n--- Testing Candidate: {cand} ---")
            for w in [360, 390, 412]:
                page = await browser.new_page(viewport={'width': w, 'height': 800})
                await page.goto(url)
                await page.add_style_tag(content=css)
                await page.evaluate('applyLanguage("bn")')
                
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
                diff = motto_w - brand_w
                pct = motto_w / brand_w * 100
                print(f"  w={w}px: Brand={brand_w:.1f}px, Motto={motto_w:.1f}px (diff: {diff:+.1f}px, {pct:.1f}%)")
                await page.close()
                
        await browser.close()

asyncio.run(find_bn_perfect_clamp())

