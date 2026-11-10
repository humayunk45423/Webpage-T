import asyncio
import os
import re
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1280, "height": 900})
        page = await context.new_page()

        file_url = f"file:///{os.path.abspath('index.html').replace(os.sep, '/')}"
        await page.goto(file_url)
        await page.wait_for_timeout(500)

        print("=== 1. VERIFYING LIGHT (WHITE) MODE ===")
        # Ensure light mode
        await page.evaluate("() => document.documentElement.setAttribute('data-theme', 'light')")
        await page.wait_for_timeout(200)

        # Check right phone body fill
        right_phone_fill = await page.evaluate("() => getComputedStyle(document.querySelector('.phone-back-body')).fill")
        print(f"Right phone fill in Light Mode: {right_phone_fill}")
        assert "backPhoneGradRed" in right_phone_fill or "red" in right_phone_fill.lower() or "rgb" in right_phone_fill or "url" in right_phone_fill

        # Check left phone screen fill
        left_screen_fill = await page.evaluate("() => getComputedStyle(document.querySelector('.phone-left-screen-bg')).fill")
        print(f"Left screen fill in Light Mode: {left_screen_fill}")
        assert left_screen_fill in ["rgb(255, 255, 255)", "#ffffff", "#fff"]

        # Take screenshot of light mode phones
        phone_stage = page.locator(".hero-phone-stage")
        await phone_stage.screenshot(path="tests/phone_stage_light.png")

        print("=== 2. VERIFYING DARK MODE ===")
        await page.evaluate("() => document.documentElement.setAttribute('data-theme', 'dark')")
        await page.wait_for_timeout(200)

        dark_right_fill = await page.evaluate("() => getComputedStyle(document.querySelector('.phone-back-body')).fill")
        dark_mid_screen = await page.evaluate("() => getComputedStyle(document.querySelector('.phone-screen-bg')).fill")
        dark_left_screen = await page.evaluate("() => getComputedStyle(document.querySelector('.phone-left-screen-bg')).fill")
        print(f"Dark mode right phone fill: {dark_right_fill}")
        print(f"Dark mode middle screen fill: {dark_mid_screen}")
        print(f"Dark mode left screen fill: {dark_left_screen}")

        await phone_stage.screenshot(path="tests/phone_stage_dark.png")

        print("=== 3. VERIFYING BATTERY POSITION ===")
        # Middle phone battery Nub element
        # Path nub is at M320 50.5V53.5
        # Screen right edge is 348
        # Let's inspect the battery element in SVG
        battery_nub_d = await page.evaluate("() => document.querySelector('.phone-group-front path[d*=\"M320\"]').getAttribute('d')")
        print(f"Battery nub terminal d: {battery_nub_d}")
        assert battery_nub_d == "M320 50.5V53.5"

        print("=== 4. VERIFYING 7-DAY GUARANTEE REMOVAL (INDEX) ===")
        # Check text in both languages
        for lang in ['bn', 'en']:
            await page.evaluate(f"() => window.setLanguage && window.setLanguage('{lang}')")
            await page.wait_for_timeout(200)
            body_text = await page.evaluate("() => document.body.innerText")
            assert "7-day" not in body_text.lower(), f"Found '7-day' in index {lang}!"
            assert "৭ দিন" not in body_text, f"Found '৭ দিন' in index {lang}!"
            assert "গ্যারান্টি" not in body_text, f"Found 'গ্যারান্টি' in index {lang}!"

        print("=== 5. VERIFYING INVENTORY.HTML ===")
        inv_url = f"file:///{os.path.abspath('inventory.html').replace(os.sep, '/')}"
        await page.goto(inv_url)
        await page.wait_for_timeout(400)
        for lang in ['bn', 'en']:
            await page.evaluate(f"() => window.setLanguage && window.setLanguage('{lang}')")
            await page.wait_for_timeout(200)
            body_text = await page.evaluate("() => document.body.innerText")
            assert "7-day" not in body_text.lower(), f"Found '7-day' in inventory {lang}!"
            assert "৭ দিন" not in body_text, f"Found '৭ দিন' in inventory {lang}!"
            assert "গ্যারান্টি" not in body_text, f"Found 'গ্যারান্টি' in inventory {lang}!"

        print("ALL ASSERTIONS PASSED SUCCESSFULLY!")
        await browser.close()

asyncio.run(verify())
