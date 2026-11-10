from PIL import Image

def inspect_y(path):
    img = Image.open(path).convert("RGB")
    # let's print the bottom 5 rows of non-white pixels
    print(f"=== {path} ===")
    for y in range(img.height - 10, img.height):
        row_colors = [img.getpixel((x, y)) for x in range(img.width)]
        non_white = [c for c in row_colors if c != (255, 255, 255)]
        print(f"Row {y}: {len(non_white)} colored pixels")

inspect_y("tests/buy_clipped.png")
inspect_y("tests/buy_fixed.png")

