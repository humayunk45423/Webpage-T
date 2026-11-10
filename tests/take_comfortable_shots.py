from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

css = """
/* Desktop Badge */
.hero-badge.apple-specialist-badge {
    font-size: clamp(0.78rem, 1.0vw, 0.88rem) !important;
    padding: 6px 16px !important;
    white-space: nowrap !important;
    line-height: 1.35 !important;
}
.hero-badge.apple-specialist-badge i {
    font-size: 1.05rem !important;
}

/* Desktop Title */
.hero-title {
    font-size: clamp(2.3rem, 3.3vw, 3.3rem) !important;
    font-weight: 900 !important;
    letter-spacing: -0.025em !important;
    line-height: 1.22 !important;
    margin-bottom: 18px !important;
    text-align: left !important;
    padding: 4px 0 !important;
}
.hero-brand-name {
    display: block !important;
    line-height: 1.18 !important;
    margin-bottom: 4px !important;
    padding: 2px 0 !important;
    white-space: nowrap !important;
}
.hero-motto {
    display: block !important;
    line-height: 1.24 !important;
    margin-top: 0 !important;
    padding: 3px 2px 5px !important;
    white-space: nowrap !important;
}

@media (max-width: 768px) {
    .hero-badge.apple-specialist-badge {
        font-size: clamp(0.69rem, 2.75vw, 0.80rem) !important;
        padding: 5px 14px !important;
        white-space: nowrap !important;
        line-height: 1.32 !important;
        gap: 7px !important;
    }
    .hero-badge.apple-specialist-badge i {
        font-size: 0.95rem !important;
    }
    .hero-title {
        font-size: clamp(1.58rem, 6.5vw, 2.12rem) !important;
        line-height: 1.22 !important;
        letter-spacing: -0.02em !important;
        margin-bottom: 12px !important;
        text-align: center !important;
        padding: 3px 0 !important;
    }
    .hero-brand-name {
        line-height: 1.16 !important;
        margin-bottom: 3px !important;
        padding: 1px 0 !important;
    }
    .hero-motto {
        line-height: 1.22 !important;
        padding: 2px 2px 4px !important;
    }
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # 1. Mobile BN
    page = browser.new_page(viewport={"width": 360, "height": 740})
    page.goto(url)
    page.add_style_tag(content=css)
    page.evaluate("applyLanguage('bn')")
    page.wait_for_timeout(200)
    page.locator("#hero").screenshot(path="tests/preview_comfortable_mob_bn.png")
    
    # 2. Mobile EN
    page.evaluate("applyLanguage('en')")
    page.wait_for_timeout(200)
    page.locator("#hero").screenshot(path="tests/preview_comfortable_mob_en.png")
    page.close()
    
    # 3. Desktop BN & EN
    page_d = browser.new_page(viewport={"width": 1440, "height": 900})
    page_d.goto(url)
    page_d.add_style_tag(content=css)
    page_d.evaluate("applyLanguage('bn')")
    page_d.wait_for_timeout(200)
    page_d.locator("#hero").screenshot(path="tests/preview_comfortable_desk_bn.png")
    
    page_d.evaluate("applyLanguage('en')")
    page_d.wait_for_timeout(200)
    page_d.locator("#hero").screenshot(path="tests/preview_comfortable_desk_en.png")
    page_d.close()
    
    browser.close()
print("Comfortably big screenshots saved!")

