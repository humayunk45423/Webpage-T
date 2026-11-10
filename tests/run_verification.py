import os
import sys
from playwright.sync_api import sync_playwright

os.makedirs('tests/after', exist_ok=True)
url = 'file:///' + os.path.abspath('index.html').replace('\\', '/')

viewports = [
    ('desktop', 1440, 900),
    ('tablet', 820, 1180),
    ('mobile', 390, 844),
    ('mobile_small', 360, 640)
]

errors = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    for name, w, h in viewports:
        for theme in ['light', 'dark']:
            for lang in ['bn', 'en']:
                page = browser.new_page(viewport={'width': w, 'height': h})
                page.on('console', lambda msg: errors.append(f"Console error: {msg.text}") if msg.type == 'error' else None)
                page.on('pageerror', lambda exc: errors.append(f"Page error: {exc}"))
                
                page.goto(url)
                page.evaluate(f'''() => {{
                    applyTheme('{theme}');
                    applyLanguage('{lang}');
                }}''')
                page.wait_for_timeout(350)
                
                # Check chip text
                chip1_text = page.locator('.chip-1 .chip-text').text_content()
                if lang == 'bn' and 'যাচাইকৃত' not in chip1_text:
                    errors.append(f"BN chip 1 text mismatch: {chip1_text}")
                elif lang == 'en' and 'Verified' not in chip1_text:
                    errors.append(f"EN chip 1 text mismatch: {chip1_text}")
                
                # Check 360x640 fold
                if name == 'mobile_small':
                    title_box = page.locator('.hero-title').bounding_box()
                    btn_box = page.locator('.hero-actions .btn-primary').bounding_box()
                    if btn_box and (btn_box['y'] + btn_box['height'] > 640):
                        print(f"Warning: on {name}_{theme}_{lang}, btn bottom is {btn_box['y'] + btn_box['height']}")
                    else:
                        print(f"Fold check PASS: on {name}_{theme}_{lang}, btn bottom is {btn_box['y'] + btn_box['height']} (fold is 640)")
                
                hero = page.locator('#hero')
                hero.screenshot(path=f'tests/after/{name}_{theme}_{lang}.png')
                page.close()
                
    browser.close()

if errors:
    print(f"FAILED with {len(errors)} issues:")
    for err in errors:
        print(" - ", err)
    sys.exit(1)
else:
    print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
