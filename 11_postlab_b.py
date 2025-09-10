
from PIL import Image, ImageOps

img = Image.open(r'C:\Users\mendp\OneDrive\Pictures\MU.jpg')
padded = ImageOps.expand(img, border=20, fill='black')
padded.show()