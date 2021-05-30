"""This code deals with compressing JPEGs.
The idea is that you have a set of images that are then randomly compressed to a resolution between 10% and 90% of the original quality.
Both the fullsized and the compressed pictures are stored in two different lists that are then accessed by the Code_experimental_desing.py document."""

#Importing essential functions
from psychopy import visual, core, event
from PIL import Image
import PIL
import os
import glob
import random

#Importing images from the Stock_files_library
"""In this part, a list of images (represented by image_list) is imported out of the Stock_files_library."""

from Stock_files_library import image_list


#Creating different resolutions
"""In this part, I create a list to represent different states of JPEG compression.
The resolution list contains the different sizes that pictures will be randomly compressed to.
Each number represents a percentage of quality compared to the original image.
The picture_sizes list will contain the actual resolution of the compressed image for each trial."""

resolution = [10, 20, 30, 40, 50, 60, 70, 80, 90]
picture_sizes = []
#Implementing JPEG compression
"""In this part, I initialize the compression_trial function that compresses JPEG images to a random size and saves them in a different file.
The for loop ensures that the compression process will take place 50 times - which is the number of trials in the experiment - by using the range function.
The compressed_images list is empty at the beginning but all compressed images will be saved there.
The im object opens a random picture out of the image_list of original jpegs.
The im.save function saves the im as a new JPEG under the name "Full_image.jpg" with the number of the current trial added into the files name.
The im2 object opens the just saved Full_image.jpg of the current trial.
The im2.save function compresses the picture to a random quality between 10 and 90% (represented by the resolution list) and stores
the new image as "Compressed_image.jpg" with the number of the current trial added into it."""

path = "./Images"
def compression_trial():
    #resolutions = []
    for i in range(50):
        compressed_images = []
        pixelation = random.choice(resolution)
        im = Image.open(random.choice(image_list))
        os.chdir(path)
        im.save("Full_image" + str(i) +".jpg", optimize = True, quality=100)
        im2 = Image.open("Full_image" + str(i) + ".jpg")
        im2.save ("Compressed_image" + str(i) +".jpg", optimize = True, quality = pixelation)
        picture_sizes.append(pixelation)


#Executing JPEG compression
"""In this part, the compression_trial function is executed."""
compression_trial()


#Creating list of Compressed pictures
"""In this part I create a list of compressed images that can then be accessed by the Code_experimental_design.py file.
Each comp_image_1 to comp_image_50 object stores one of the just created compressed image files.
In the compressed_image list, all the comp_image objects are subsequentally stored."""

comp_image_1 = "./Images/Compressed_image0.jpg"
comp_image_2 = "./Images/Compressed_image1.jpg"
comp_image_3 = "./Images/Compressed_image2.jpg"
comp_image_4 = "./Images/Compressed_image3.jpg"
comp_image_5 = "./Images/Compressed_image4.jpg"
comp_image_6 = "./Images/Compressed_image5.jpg"
comp_image_7 = "./Images/Compressed_image6.jpg"
comp_image_8 = "./Images/Compressed_image7.jpg"
comp_image_9 = "./Images/Compressed_image8.jpg"
comp_image_10 = "./Images/Compressed_image9.jpg"
comp_image_11 = "./Images/Compressed_image10.jpg"
comp_image_12 = "./Images/Compressed_image11.jpg"
comp_image_13 = "./Images/Compressed_image12.jpg"
comp_image_14 = "./Images/Compressed_image13.jpg"
comp_image_15 = "./Images/Compressed_image14.jpg"
comp_image_16 = "./Images/Compressed_image15.jpg"
comp_image_17 = "./Images/Compressed_image16.jpg"
comp_image_18 = "./Images/Compressed_image17.jpg"
comp_image_19 = "./Images/Compressed_image18.jpg"
comp_image_20 = "./Images/Compressed_image19.jpg"
comp_image_21 = "./Images/Compressed_image20.jpg"
comp_image_22 = "./Images/Compressed_image21.jpg"
comp_image_23 = "./Images/Compressed_image22.jpg"
comp_image_24 = "./Images/Compressed_image23.jpg"
comp_image_25 = "./Images/Compressed_image24.jpg"
comp_image_26 = "./Images/Compressed_image25.jpg"
comp_image_27 = "./Images/Compressed_image26.jpg"
comp_image_28 = "./Images/Compressed_image27.jpg"
comp_image_29 = "./Images/Compressed_image28.jpg"
comp_image_30 = "./Images/Compressed_image29.jpg"
comp_image_31 = "./Images/Compressed_image30.jpg"
comp_image_32 = "./Images/Compressed_image31.jpg"
comp_image_33 = "./Images/Compressed_image32.jpg"
comp_image_34 = "./Images/Compressed_image33.jpg"
comp_image_35 = "./Images/Compressed_image34.jpg"
comp_image_36 = "./Images/Compressed_image35.jpg"
comp_image_37 = "./Images/Compressed_image36.jpg"
comp_image_38 = "./Images/Compressed_image37.jpg"
comp_image_39 = "./Images/Compressed_image38.jpg"
comp_image_40 = "./Images/Compressed_image39.jpg"
comp_image_41 = "./Images/Compressed_image40.jpg"
comp_image_42 = "./Images/Compressed_image41.jpg"
comp_image_43 = "./Images/Compressed_image42.jpg"
comp_image_44 = "./Images/Compressed_image43.jpg"
comp_image_45 = "./Images/Compressed_image44.jpg"
comp_image_46 = "./Images/Compressed_image45.jpg"
comp_image_47 = "./Images/Compressed_image46.jpg"
comp_image_48 = "./Images/Compressed_image47.jpg"
comp_image_49 = "./Images/Compressed_image48.jpg"
comp_image_50 = "./Images/Compressed_image49.jpg"


compressed_images = [comp_image_1, comp_image_2, comp_image_3, comp_image_4, comp_image_5, comp_image_6, comp_image_7,
                     comp_image_8, comp_image_9, comp_image_10, comp_image_11, comp_image_12,comp_image_13, comp_image_14,
                     comp_image_15, comp_image_16, comp_image_17, comp_image_18, comp_image_19,
                     comp_image_20, comp_image_21, comp_image_22, comp_image_23, comp_image_24,
                     comp_image_25,comp_image_26, comp_image_27, comp_image_28, comp_image_29, comp_image_30,
                     comp_image_31, comp_image_32, comp_image_33, comp_image_34, comp_image_35, comp_image_36,
                     comp_image_37,comp_image_38, comp_image_39, comp_image_40, comp_image_41, comp_image_42,
                     comp_image_43, comp_image_44, comp_image_45, comp_image_46, comp_image_47, comp_image_48,
                     comp_image_49, comp_image_50]


#Creating list of Fullsized pictures
"""In this part I create a list of fullsized images that can then be accessed by the Code_experimental_design.py file.
Each full_image_1 to full_image_50 object stores one of the just created fullsized image files.
In the full_images list, all the full_image objects are subsequentally stored."""

full_image_1 = "./Images/Full_image0.jpg"
full_image_2 = "./Images/Full_image1.jpg"
full_image_3 = "./Images/Full_image2.jpg"
full_image_4 = "./Images/Full_image3.jpg"
full_image_5 = "./Images/Full_image4.jpg"
full_image_6 = "./Images/Full_image5.jpg"
full_image_7 = "./Images/Full_image6.jpg"
full_image_8 = "./Images/Full_image7.jpg"
full_image_9 = "./Images/Full_image8.jpg"
full_image_10 = "./Images/Full_image9.jpg"
full_image_11 = "./Images/Full_image10.jpg"
full_image_12 = "./Images/Full_image11.jpg"
full_image_13 = "./Images/Full_image12.jpg"
full_image_14 = "./Images/Full_image13.jpg"
full_image_15 = "./Images/Full_image14.jpg"
full_image_16 = "./Images/Full_image15.jpg"
full_image_17 = "./Images/Full_image16.jpg"
full_image_18 = "./Images/Full_image17.jpg"
full_image_19 = "./Images/Full_image18.jpg"
full_image_20 = "./Images/Full_image19.jpg"
full_image_21 = "./Images/Full_image20.jpg"
full_image_22 = "./Images/Full_image21.jpg"
full_image_23 = "./Images/Full_image22.jpg"
full_image_24 = "./Images/Full_image23.jpg"
full_image_25 = "./Images/Full_image24.jpg"
full_image_26 = "./Images/Full_image25.jpg"
full_image_27 = "./Images/Full_image26.jpg"
full_image_28 = "./Images/Full_image27.jpg"
full_image_29 = "./Images/Full_image28.jpg"
full_image_30 = "./Images/Full_image29.jpg"
full_image_31 = "./Images/Full_image30.jpg"
full_image_32 = "./Images/Full_image31.jpg"
full_image_33 = "./Images/Full_image32.jpg"
full_image_34 = "./Images/Full_image33.jpg"
full_image_35 = "./Images/Full_image34.jpg"
full_image_36 = "./Images/Full_image35.jpg"
full_image_37 = "./Images/Full_image36.jpg"
full_image_38 = "./Images/Full_image37.jpg"
full_image_39 = "./Images/Full_image38.jpg"
full_image_40 = "./Images/Full_image39.jpg"
full_image_41 = "./Images/Full_image40.jpg"
full_image_42 = "./Images/Full_image41.jpg"
full_image_43 = "./Images/Full_image42.jpg"
full_image_44 = "./Images/Full_image43.jpg"
full_image_45 = "./Images/Full_image44.jpg"
full_image_46 = "./Images/Full_image45.jpg"
full_image_47 = "./Images/Full_image46.jpg"
full_image_48 = "./Images/Full_image47.jpg"
full_image_49 = "./Images/Full_image48.jpg"
full_image_50 = "./Images/Full_image49.jpg"

full_images = [full_image_1, full_image_2, full_image_3, full_image_4, full_image_5, full_image_6, full_image_7,
               full_image_8,full_image_9,full_image_10, full_image_11, full_image_12,full_image_13, full_image_14,
               full_image_15, full_image_16, full_image_17, full_image_18, full_image_19,
               full_image_20,full_image_21,full_image_22, full_image_23, full_image_24,
               full_image_25, full_image_26, full_image_27, full_image_28, full_image_29, full_image_30, full_image_31,
               full_image_32,full_image_33,full_image_34, full_image_35, full_image_36,
               full_image_37, full_image_38, full_image_39, full_image_40, full_image_41, full_image_42, full_image_43,
               full_image_44,full_image_45,full_image_46, full_image_47, full_image_48, full_image_49, full_image_50]










