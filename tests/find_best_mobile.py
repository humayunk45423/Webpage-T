from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

def test_combination(t_size_mob, b_size_mob):
    css = f"""
    @media (max-width: 768px) {{
        .hero-badge.apple-specialist-badge {{
            font-size: {b_size_mob} !important;
            padding: 5px 12px !important;
            white-space: nowrap !important;
        }}
        .hero-badge.apple-specialist-badge i {{
            font-size: 0.95rem !important;
        }}
        .hero-title {{
            font-size: {t_size_mob} !important;
            line-height: 1.22 !important;
            padding: 3px 0 !important;
        }}
        .hero-brand-name {{
            line-height: 1.18 !important;
            margin-bottom: 3px !important;
            white-space: nowrap !important;
        }}
        .hero-motto {{
            line-height: 1.24 !important;
            padding: 2px 2px 4px !important;
            white-space: nowrap !important;
        }}
    }}
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for w in [360, 375, 390, 412]:
            page = browser.new_page(viewport={"width": w, "height": 740})
            page.goto(url)
            page.add_style_tag(content=css)
            for lang in ['bn', 'en']:
                page.evaluate(f"applyLanguage('{lang}')")
                page.wait_for_timeout(100)
                badge_box = page.locator(".hero-badge.apple-specialist-badge").bounding_box()
                title_box = page.locator(".hero-title").bounding_box()
                scroll_w = page.evaluate("document.documentElement.scrollWidth")
                
                # Check if badge or title overflows
                badge_fits = badge_box['x'] >= 0 and (badge_box['x'] + badge_box['width']) <= w
                overflow = scroll_w > w
                assert not overflow, f"Overflow on w={w} {lang}! scroll_w={scroll_w}"
                assert badge_fits, f"Badge overflow on w={w} {lang}! badge_box={badge_box}"
            page.close()
        browser.close()
    print(f"Passed: title={t_size_mob}, badge={b_size_mob}")

print("Testing combinations...")
test_combination("clamp(1.55rem, 6.4vw, 2.1rem)", "clamp(0.68rem, 2.7vw, 0.78rem)")
test_combination("clamp(1.6rem, 6.6vw, 2.15rem)", "clamp(0.70rem, 2.75vw, 0.80rem)")
test_combination("clamp(1.58rem, 6.5vw, 2.12rem)", "clamp(0.69rem, 2.72vw, 0.79rem)")

