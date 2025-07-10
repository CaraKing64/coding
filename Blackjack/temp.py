from hashlib import new
import os
from PIL import Image


path= r"c:/Users/isaac/Documents/Coding/Blackjack/img/resize/"

dir = os.listdir(path)
#print(dir)

for file in dir:
    img = Image.open(file)
    img.thumbnail(128)
    img.save(file)