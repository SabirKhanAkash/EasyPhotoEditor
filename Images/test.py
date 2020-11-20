from PIL import Image, ImageDraw
from PIL import ImageFont
import PIL.ImageFont
from PIL import ImageEnhance
image = Image.open("3Copy.jpg")

en_img = PIL.ImageEnhance._Enhance()
en_img.enhance(1.5).show()

