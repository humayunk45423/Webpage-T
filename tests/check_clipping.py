from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    page.evaluate("applyLanguage('en')")
    page.evaluate("applyTheme('light')")
    page.wait_for_timeout(300)
    
    # Screenshot the hero title in English
    title = page.locator(".hero-title")
    title.screenshot(path="tests/title_en_clipped.png")
    
    page.evaluate("applyLanguage('bn')")
    page.wait_for_timeout(300)
    title.screenshot(path="tests/title_bn_clipped.png")
    
    page.close()
    browser.close()
print("Screenshots taken")

