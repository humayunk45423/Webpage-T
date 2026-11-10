from PIL import Image

img = Image.open("tests/cand_title_en.png")
for x in range(img.width):
    p = img.getpixel((x, 0))
    if p[0] < 230 or p[1] < 230 or p[2] < 230:
        print(f"Triggered at x={x}: {p}")
        break

