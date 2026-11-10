from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

def check_motto_scroll_width(title_size_mob, badge_size_mob):
    css = f"""
    @media (max-width: 768px) {{
        .hero-badge.apple-specialist-badge {{
            font-size: {badge_size_mob} !important;
            padding: 5px 14px !important;
            white-space: nowrap !important;
        }}
        .hero-badge.apple-specialist-badge i {{
            font-size: 0.95rem !important;
        }}
        .hero-title {{
            font-size: {title_size_mob} !important;
            line-height: 1.2 !important;
            padding: 2px 0 !important;
        }}
        .hero-brand-name {{
            line-height: 1.16 !important;
            margin-bottom: 3px !important;
            white-space: nowrap !important;
        }}
        .hero-motto {{
            line-height: 1.22 !important;
            padding: 2px 2px 4px !important;
            white-space: nowrap !important;
        }}
    }}
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 360, "height": 740})
        page.goto(url)
        page.add_style_tag(content=css)
        for lang in ['bn', 'en']:
            page.evaluate(f"applyLanguage('{lang}')")
            page.wait_for_timeout(100)
            
            # check scrollWidth vs clientWidth of hero-motto, hero-brand-name, and badge
            motto_sw = page.eval_on_selector(".hero-motto", "el => el.scrollWidth")
            motto_cw = page.eval_on_selector(".hero-motto", "el => el.clientWidth")
            brand_sw = page.eval_on_selector(".hero-brand-name", "el => el.scrollWidth")
            brand_cw = page.eval_on_selector(".hero-brand-name", "el => el.clientWidth")
            badge_sw = page.eval_on_selector(".hero-badge.apple-specialist-badge", "el => el.scrollWidth")
            card_cw = page.eval_on_selector(".hero-section", "el => el.clientWidth")
            
            print(f"[{lang.upper()}] card={card_cw}px | badge={badge_sw}px | brand_sw={brand_sw}px (container={brand_cw}) | motto_sw={motto_sw}px (container={motto_cw})")
        page.close()
        browser.close()

for t_size in [
    "clamp(1.48rem, 5.8vw, 1.95rem)",
    "clamp(1.55rem, 6.2vw, 2.05rem)",
    "clamp(1.62rem, 6.5vw, 2.15rem)"
]:
    print(f"\n--- Testing mobile title size: {t_size} ---")
    check_motto_scroll_width(t_size, "clamp(0.66rem, 2.7vw, 0.78rem)")

