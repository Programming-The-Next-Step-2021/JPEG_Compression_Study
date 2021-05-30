"""This file is just the library of all the different stock photo images that will be used in the experiment.
All those images are free to use, have similar quality and show similar landscape motives.
This document will be both accessed by the Code_experimental_design.py and the Compression_code.py file."""

#Import essential functions from python
from PIL import Image
import PIL
import os
import glob
import random
from psychopy import visual, core, event

#Storing images
"""In this part, all of the different pictures are stored in a list.
Each of the image_1 to image_10 objects stores a jpg file.
The image_list list consists of all the just created images and can be accessed by both the Code_experimental_design.py and the Compression_code.py file"""

image_1 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_1.jpg"
image_2 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_2.jpg"
image_3 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_3.jpg"
image_4 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_4.jpg"
image_5 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_5.jpg"
image_6 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_6.jpg"
image_7 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_7.jpg"
image_8 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_8.jpg"
image_9 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_9.jpg"
image_10 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Stock_images/Image_10.jpg"

image_list = [image_1, image_2, image_3,image_4,image_5,
              image_6,image_7,image_8,image_9,image_10]

