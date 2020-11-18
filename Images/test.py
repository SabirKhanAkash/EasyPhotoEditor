from PIL import Image, ImageDraw
from PIL import ImageFont
import PIL.ImageFont
image = Image.open("3Copy.jpg")

a=150
b=20
font_type1 = ImageFont.truetype('',18)
draw = ImageDraw.Draw(image)
draw.text(xy=(a,b),text="Hello World",fill=(255,69,200),font=font_type1)

image.show()