from playwright.sync_api import sync_playwright
import os

url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url)
    
    measure_script = """
    function measure(selector) {
        const el = document.querySelector(selector);
        const style = window.getComputedStyle(el);
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        ctx.font = `${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
        return {
            text: el.innerText.trim(),
            width: ctx.measureText(el.innerText.trim()).width,
            fontSize: style.fontSize
        };
    }
    window.measure = measure;
    """
    page.add_script_tag(content=measure_script)
    
    for t_size in [
        "clamp(2.2rem, 3.1vw, 3.1rem)",
        "clamp(2.3rem, 3.3vw, 3.3rem)",
        "clamp(2.4rem, 3.5vw, 3.5rem)"
    ]:
        page.add_style_tag(content=f".hero-title {{ font-size: {t_size} !important; }}")
        col_w = page.eval_on_selector(".hero-content-col", "el => el.clientWidth")
        print(f"\n=== Desktop Title: {t_size} (Content Col width = {col_w}px) ===")
        for lang in ['bn', 'en']:
            page.evaluate(f"applyLanguage('{lang}')")
            res_brand = page.evaluate("measure('.hero-brand-name')")
            res_motto = page.evaluate("measure('.hero-motto')")
            print(f"[{lang.upper()}] Brand: '{res_brand['text']}' -> {res_brand['width']:.1f}px (font: {res_brand['fontSize']})")
            print(f"[{lang.upper()}] Motto: '{res_motto['text']}' -> {res_motto['width']:.1f}px (font: {res_motto['fontSize']})")
            
    page.close()
    browser.close()

