from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    
    # Check all sections in Light & Dark, BN & EN
    for theme in ['light', 'dark']:
        for lang in ['bn', 'en']:
            page.evaluate(f"applyTheme('{theme}')")
            page.evaluate(f"applyLanguage('{lang}')")
            page.wait_for_timeout(200)
            
            # Take close-up screenshots of hero title
            title = page.locator(".hero-title")
            title.screenshot(path=f"tests/title_check_{theme}_{lang}.png")
            
    page.close()
    browser.close()
print("All title checks saved")

