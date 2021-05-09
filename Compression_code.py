#This is going to be the code for the JPEG compression


from PIL import Image
import PIL
import os
import glob
dir(Image)
#print(dir(Image))

im = Image.open("P4112976.JPG")
print(f"The image size dimensions are: {im.size}")
im.show()

file_name = "image-1-compressed.jpg"
dim = im.size
print(f"this is the current size of the picture: {dim}")

im.save("Compressed_"+file_name, optimize = True, quality=30)

im2 = Image.open("Compressed_image-1-compressed.jpg")
im2.show()





