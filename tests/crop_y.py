from PIL import Image

def find_y_crop(path, out_crop):
    img = Image.open(path).convert("RGBA")
    # crop region around "Buy"
    # Buy is around x=0..120, y=30..110
    cropped = img.crop((0, 30, 150, img.height))
    cropped.save(out_crop)

find_y_crop("tests/title_en_clipped.png", "tests/buy_clipped.png")
find_y_crop("tests/title_en_fixed.png", "tests/buy_fixed.png")
print("Saved crops")

