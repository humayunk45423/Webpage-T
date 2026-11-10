from PIL import Image

img = Image.open("tests/cand_title_en.png")
for y in range(10):
    row_colors = [img.getpixel((x, y)) for x in range(img.width)]
    dark = [c for c in row_colors if c[0] < 200]
    print(f"Row {y}: {len(dark)} dark pixels")

