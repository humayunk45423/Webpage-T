from playwright.sync_api import sync_playwright
import os
import shutil

artifact_dir = r"C:\Users\Humayoun\.gemini\antigravity\brain\6b0b4198-e2d4-4f1d-aa9e-fb7b77d018d7\hero_redesign_shots"
os.makedirs(artifact_dir, exist_ok=True)
os.makedirs("tests/after", exist_ok=True)

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

viewports = {
    "desktop": {"width": 1440, "height": 900},
    "mobile": {"width": 390, "height": 844},
    "mobile_small": {"width": 360, "height": 740}
}

modes = [
    ("dark", "bn"),
    ("dark", "en"),
    ("light", "bn"),
    ("light", "en")
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    for vp_name, vp in viewports.items():
        for theme, lang in modes:
            page = browser.new_page(viewport=vp)
            page.goto(url)
            page.evaluate(f"applyTheme('{theme}')")
            page.evaluate(f"applyLanguage('{lang}')")
            page.wait_for_timeout(400)
            
            hero = page.locator("#hero")
            filename = f"after_{vp_name}_{theme}_{lang}.png"
            local_path = os.path.join("tests/after", filename)
            art_path = os.path.join(artifact_dir, filename)
            
            hero.screenshot(path=local_path)
            shutil.copyfile(local_path, art_path)
            print(f"Captured: {filename}")
            page.close()
            
    browser.close()
print("All screenshots generated and saved to artifact directory!")

