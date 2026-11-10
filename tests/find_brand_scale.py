import asyncio
import os
from playwright.async_api import async_playwright

async def find_exact_scale():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        await page.goto(url)
        
        candidates = [
            "clamp(2.1rem, 9.6vw, 2.45rem)",
            "clamp(2.15rem, 9.8vw, 2.42rem)",
            "clamp(2.2rem, 10.0vw, 2.46rem)",
            "clamp(2.05rem, 9.8vw, 2.40rem)",
            "clamp(2.1rem, 9.8vw, 2.42rem)"
        ]
        
        for cand in candidates:
            css = f"""
            .hero-brand-name {{
                font-size: {cand} !important;
                letter-spacing: -0.02em;
            }}
            """
            await page.add_style_tag(content=css)
            print(f"\nTesting Candidate: {cand}")
            
            for w in [360, 390, 412]:
                await page.set_viewport_size({'width': w, 'height': 800})
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
                    scroll_w = await page.evaluate("() => document.documentElement.scrollWidth")
                    client_w = await page.evaluate("() => document.documentElement.clientWidth")
                    print(f"  w={w} {lang}: Badge={badge_w:.1f}px, Brand={brand_w:.1f}px ({brand_w/badge_w*100:.1f}%), Overflow={scroll_w > client_w}")
                    
        await browser.close()

asyncio.run(find_exact_scale())

