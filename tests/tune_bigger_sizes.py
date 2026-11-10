from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

def test_sizes(title_size_mob, title_size_desk, badge_size_mob, badge_size_desk):
    css = f"""
    .hero-badge.apple-specialist-badge {{
        font-size: {badge_size_desk} !important;
        padding: 6px 16px !important;
        white-space: nowrap !important;
    }}
    .hero-badge.apple-specialist-badge i {{
        font-size: 1.05rem !important;
    }}
    .hero-title {{
        font-size: {title_size_desk} !important;
        line-height: 1.2 !important;
        padding: 4px 0 !important;
    }}
    .hero-brand-name {{
        line-height: 1.18 !important;
        margin-bottom: 4px !important;
        white-space: nowrap !important;
    }}
    .hero-motto {{
        line-height: 1.24 !important;
        padding: 3px 2px 5px !important;
        white-space: nowrap !important;
    }}
    
    @media (max-width: 768px) {{
        .hero-badge.apple-specialist-badge {{
            font-size: {badge_size_mob} !important;
            padding: 5px 13px !important;
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
        }}
        .hero-motto {{
            line-height: 1.22 !important;
            padding: 2px 2px 4px !important;
        }}
    }}
    """
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Test 1: Desktop 1440
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url)
        page.add_style_tag(content=css)
        for lang in ['bn', 'en']:
            page.evaluate(f"applyLanguage('{lang}')")
            page.wait_for_timeout(100)
            motto_box = page.locator(".hero-motto").bounding_box()
            brand_box = page.locator(".hero-brand-name").bounding_box()
            badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
            title_box = page.locator(".hero-title").bounding_box()
            scroll_w = page.evaluate("document.documentElement.scrollWidth")
            print(f"[Desktop 1440 {lang.upper()}] Title h={title_box['height']:.1f}, Badge w={badge_box['width']:.1f}, Motto w={motto_box['width']:.1f}, h={motto_box['height']:.1f}, overflow={scroll_w > 1440}")
        page.close()
        
        # Test 2: Mobile 360
        page = browser.new_page(viewport={"width": 360, "height": 740})
        page.goto(url)
        page.add_style_tag(content=css)
        for lang in ['bn', 'en']:
            page.evaluate(f"applyLanguage('{lang}')")
            page.wait_for_timeout(100)
            motto_box = page.locator(".hero-motto").bounding_box()
            brand_box = page.locator(".hero-brand-name").bounding_box()
            badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
            title_box = page.locator(".hero-title").bounding_box()
            scroll_w = page.evaluate("document.documentElement.scrollWidth")
            print(f"[Mobile 360 {lang.upper()}] Title h={title_box['height']:.1f}, Badge w={badge_box['width']:.1f}, Motto w={motto_box['width']:.1f}, h={motto_box['height']:.1f}, overflow={scroll_w > 360}")
        page.close()
        
        browser.close()

print("Testing Option 1: Mobile title clamp(1.65rem, 6.6vw, 2.05rem), desktop clamp(2.3rem, 3.2vw, 3.2rem)")
test_sizes(
    title_size_mob="clamp(1.65rem, 6.6vw, 2.05rem)",
    title_size_desk="clamp(2.3rem, 3.2vw, 3.2rem)",
    badge_size_mob="clamp(0.68rem, 2.8vw, 0.78rem)",
    badge_size_desk="clamp(0.78rem, 1.0vw, 0.88rem)"
)

