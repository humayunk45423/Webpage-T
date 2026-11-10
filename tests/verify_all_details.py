from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Check Mobile 360x640: Menu button and Title lines
    page_m = browser.new_page(viewport={"width": 360, "height": 740})
    page_m.goto(url)
    page_m.evaluate("applyLanguage('bn')")
    page_m.wait_for_timeout(300)
    
    # 1. Hamburger button visible and within viewport
    menu_btn = page_m.locator("#menu-toggle").bounding_box()
    print("Menu toggle box:", menu_btn)
    assert menu_btn["x"] + menu_btn["width"] <= 360, f"Menu button overflows screen! {menu_btn}"
    print("  PASS: Hamburger button is fully inside the screen!")
    
    # 2. Check title lines are separate
    brand_box = page_m.locator(".hero-brand-name").bounding_box()
    motto_box = page_m.locator(".hero-motto").bounding_box()
    print("Title Line 1 (Brand):", brand_box)
    print("Title Line 2 (Motto):", motto_box)
    assert brand_box["y"] + brand_box["height"] <= motto_box["y"] + 2, "Title lines overlap or sit on the same line!"
    print("  PASS: Title Line 1 and Line 2 are on completely separate lines!")
    
    # 3. Check Dark Mode SVG Screen Background (should be WHITE)
    page_m.evaluate("applyTheme('dark')")
    page_m.wait_for_timeout(300)
    screen_fill_dark = page_m.eval_on_selector(".phone-screen-bg", "el => window.getComputedStyle(el).fill")
    print("Dark Mode Screen Fill:", screen_fill_dark)
    assert "255, 255, 255" in screen_fill_dark or "#ffffff" in screen_fill_dark, f"Dark mode screen not white: {screen_fill_dark}"
    print("  PASS: Dark mode screen is WHITE so it pops vividly against dark background!")
    
    # 4. Check Light Mode SVG Screen Background (should be DARK)
    page_m.evaluate("applyTheme('light')")
    page_m.wait_for_timeout(300)
    screen_fill_light = page_m.eval_on_selector(".phone-screen-bg", "el => window.getComputedStyle(el).fill")
    print("Light Mode Screen Fill:", screen_fill_light)
    assert "9, 11, 16" in screen_fill_light or "12, 14, 20" in screen_fill_light or "#090b10" in screen_fill_light, f"Light mode screen not dark: {screen_fill_light}"
    print("  PASS: Light mode screen is DARK so it pops vividly against light card background!")
    
    page_m.close()
    browser.close()
    print("\nALL AUTOMATED VERIFICATION CHECKS PASSED PERFECTLY!")
