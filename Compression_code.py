"""This code deals with compressing JPEGs. It´s currently in an early state
but in the end this package alone will be able to randomly compress JPEG files to any required size.
All the images that are needed aere stored in the Stock_files_library file."""

from psychopy import visual, core, event
from PIL import Image
import PIL
import os
import glob
import random

from Stock_files_library import image_list

dir(Image)
#print(dir(Image))
def compression_trial():
    im = Image.open(random.choice(image_list))
    im.save("Compressed_image.jpg", optimize = True, quality=1)
    im.show()
    im2 = Image.open("Compressed_image.jpg")
    im2.show()
    print(im.size)  
    print(im2.size)

for i in range(3):
    compression_trial()

"""This line of code compresses the JPEGs to 1% quality. More details will follow.
So far this is pretty random opening of images in full and in extremely reduced quality.
I still have to figure out, how I can add the reduced images to my experimental design."""








