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

im = Image.open(random.choice(image_list))
#print(f"The image size dimensions are: {im.size}")


file_name = "image-1-compressed.jpg"
dim = im.size
#print(f"this is the current size of the picture: {dim}")

#im.save("Compressed_"+file_name, optimize = True, quality=30)
"""This line of code compresses the JPEGs to 30% quality. More details will follow"""

im2 = Image.open("Compressed_image-1-compressed.jpg")






