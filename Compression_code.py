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
resolution = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def compression_trial():
    for i in range(12):
        compressed_images = []
        im = Image.open(random.choice(image_list))
        im.save("Full_image" + str(i) +".jpg", optimize = True, quality=100)
        #im.show()
        im2 = Image.open("Full_image" + str(i) + ".jpg")
        im2.save ("Compressed_image" + str(i) +".jpg", optimize = True, quality=random.choice(resolution))
        #im2.show()







#print(compressed_images)
compression_trial()

comp_image_1 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image0.jpg"
comp_image_2 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image1.jpg"
comp_image_3 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image2.jpg"
comp_image_4 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image3.jpg"
comp_image_5 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image4.jpg"
comp_image_6 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image5.jpg"
comp_image_7 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image6.jpg"
comp_image_8 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image7.jpg"
comp_image_9 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image8.jpg"
comp_image_10 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image9.jpg"
comp_image_11 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image10.jpg"
comp_image_12 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Compressed_image11.jpg"


compressed_images = [comp_image_1, comp_image_2, comp_image_3, comp_image_4, comp_image_5, comp_image_6, comp_image_7,
                     comp_image_8, comp_image_9, comp_image_10, comp_image_11, comp_image_12]


full_image_1 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image0.jpg"
full_image_2 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image1.jpg"
full_image_3 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image2.jpg"
full_image_4 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image3.jpg"
full_image_5 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image4.jpg"
full_image_6 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image5.jpg"
full_image_7 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image6.jpg"
full_image_8 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image7.jpg"
full_image_9 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image8.jpg"
full_image_10 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image9.jpg"
full_image_11 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image10.jpg"
full_image_12 = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Full_image11.jpg"

full_images = [full_image_1, full_image_2, full_image_3, full_image_4, full_image_5, full_image_6, full_image_7,full_image_8,full_image_9,full_image_10, full_image_11, full_image_12]


"""This line of code compresses the JPEGs to 1% quality. More details will follow.
So far this is pretty random opening of images in full and in extremely reduced quality.
I still have to figure out, how I can add the reduced images to my experimental design."""








