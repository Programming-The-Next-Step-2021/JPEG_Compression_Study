"""This file is just the library of all the different stock photo images that will be used in the experiment.
So far, those images are stored locally but I will change that as soon as possible."""

from PIL import Image
import PIL
import os
import glob
import random


from psychopy import visual, core, event

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

image_list = [image_1, image_2, image_3,image_4,image_5,image_6,image_7,image_8,image_9,image_10]


#im = Image.open(random.choice(image_list))
#im.show()
