from PIL import Image

img = Image.open("tests/buy_clipped.png")
print("Pixel at 0,0:", img.getpixel((0,0)))
print("Pixel at 5,5:", img.getpixel((5,5)))
print("Pixel at 50,20 (text):", img.getpixel((50,20)))

