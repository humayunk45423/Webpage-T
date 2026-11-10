import asyncio
import os
from playwright.async_api import async_playwright

async def test_all_smart_fixes():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        url = f'file:///{os.path.abspath("index.html").replace(os.sep, "/")}'
        
        # Test CSS
        css = """
        /* 1. Chips: Remove chip-4, center chip-2 */
        .chip-4 { display: none !important; }
        .hero-phone-stage .chip-2 {
            top: 50% !important;
            transform: translateY(-50%) !important;
            right: -6% !important;
        }
        @media (max-width: 768px) {
            .hero-phone-stage .chip-2 {
                top: 50% !important;
                transform: translateY(-50%) !important;
                right: 0% !important;
            }
        }
        
        /* 2. Mobile Bengali Motto: Exact same collective length as brand name */
        @media (max-width: 768px) {
            .hero-brand-name {
                font-size: clamp(2.15rem, 10.0vw, 2.50rem) !important;
                letter-spacing: -0.025em;
                line-height: 1.22 !important;
                margin-bottom: 2px !important;
                padding: 6px 2px 5px !important;
                white-space: nowrap !important;
            }
            .lang-bn .hero-motto {
                font-size: clamp(1.72rem, 7.7vw, 1.95rem) !important;
                letter-spacing: 0 !important;
                line-height: 1.28 !important;
                margin-top: 0 !important;
                padding: 4px 2px 6px !important;
                white-space: nowrap !important;
            }
            .hero-motto {
                font-size: clamp(1.50rem, 6.4vw, 2.05rem) !important;
                letter-spacing: -0.02em;
                line-height: 1.26 !important;
                margin-top: 0 !important;
                padding: 4px 2px 6px !important;
                white-space: nowrap !important;
            }
        }
        
        /* 3. Desktop Bengali Spacing Perfection */
        @media (min-width: 769px) {
            .hero-layout {
                grid-template-columns: minmax(380px, 450px) 1fr !important;
                gap: 48px !important;
            }
            .hero-title {
                margin-bottom: 16px !important;
            }
            .hero-brand-name {
                margin-bottom: 2px !important;
                line-height: 1.16 !important;
            }
            .hero-motto {
                line-height: 1.22 !important;
            }
            .lang-bn .hero-title,
            .lang-bn .hero-brand-name,
            .lang-bn .hero-motto {
                letter-spacing: 0 !important;
            }
            .lang-bn .hero-motto {
                word-spacing: 0.08em;
            }
            .hero-desc {
                font-size: 1.05rem !important;
                line-height: 1.72 !important;
                max-width: 620px !important;
                margin-bottom: 24px !important;
            }
            .hero-actions {
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: wrap !important;
                align-items: center !important;
                gap: 14px !important;
                margin-bottom: 28px !important;
            }
            .hero-actions .btn-primary,
            .hero-actions .btn-secondary {
                padding: 13px 22px !important;
                font-size: 0.94rem !important;
                white-space: nowrap !important;
                width: auto !important;
            }
            .hero-stats-row {
                padding-top: 18px !important;
                max-width: 540px !important;
            }
            .lang-bn .stat-box h4 {
                font-weight: 800 !important;
                font-size: 1.45rem !important;
                letter-spacing: 0.02em;
            }
        }
        """
        
        # Test Desktop
        dpage = await browser.new_page(viewport={'width': 1366, 'height': 820})
        await dpage.goto(url)
        await dpage.add_style_tag(content=css)
        
        for lang in ['bn', 'en']:
            await dpage.evaluate(f'applyLanguage("{lang}")')
            for theme in ['dark', 'light']:
                await dpage.evaluate(f'applyTheme("{theme}")')
                await dpage.wait_for_timeout(100)
                await dpage.locator('#hero').screenshot(path=f"tests/smart_desk_{theme}_{lang}.png")
                
            b1 = await dpage.locator('.hero-actions .btn-primary').bounding_box()
            b2 = await dpage.locator('.hero-actions .btn-secondary').bounding_box()
            is_stacked = b2['y'] > b1['y'] + 10
            print(f"Desktop 1366px | {lang.upper()}: b1_w={b1['width']:.1f}px, b2_w={b2['width']:.1f}px, Buttons STACKED={is_stacked}")
            
        await dpage.close()
        
        # Test Mobile 390px
        mpage = await browser.new_page(viewport={'width': 390, 'height': 844})
        await mpage.goto(url)
        await mpage.add_style_tag(content=css)
        
        for lang in ['bn', 'en']:
            await mpage.evaluate(f'applyLanguage("{lang}")')
            for theme in ['dark', 'light']:
                await mpage.evaluate(f'applyTheme("{theme}")')
                await mpage.wait_for_timeout(100)
                await mpage.locator('#hero').screenshot(path=f"tests/smart_mob_{theme}_{lang}.png")
                
            brand_w = await mpage.evaluate("""() => {
                const el = document.querySelector('.hero-brand-name');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            motto_w = await mpage.evaluate("""() => {
                const el = document.querySelector('.hero-motto');
                const range = document.createRange();
                range.selectNodeContents(el);
                return range.getBoundingClientRect().width;
            }""")
            print(f"Mobile 390px | {lang.upper()}: Brand={brand_w:.1f}px, Motto={motto_w:.1f}px, Diff={abs(brand_w - motto_w):.1f}px")
            
        await mpage.close()
        await browser.close()

asyncio.run(test_all_smart_fixes())

