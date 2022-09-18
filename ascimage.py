from PIL import Image
Image.open("image.png")

import pywhatkit
pywhatkit.image_to_ascii_art('image.png', 'output.txt')
read_file = open("output.txt", "r")
print(read_file.read())
