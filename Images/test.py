from PIL import Image,ImageFilter
image = Image.open("2Copy.jpg")

image.filter(ImageFilter.BLUR).show()