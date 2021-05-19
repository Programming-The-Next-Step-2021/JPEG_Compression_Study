"""This package contains the code for the experimental design. It includes all trials step by step.
It only works if you combine it with the contents of the compression-code.py package (some of which are imported into this package).
Also it is connected to the Stock files library, which contains all important images."""
from psychopy import visual, core, event
from psychopy.hardware.keyboard import Keyboard
from psychopy.core import Clock, wait
from PIL import Image
import PIL
import os
import glob
import random

from Stock_files_library import image_list
import Compression_code

#General issues
clock = Clock()
kb = Keyboard()

#Create a window
mywin = visual.Window([1200,900], monitor = "testMonitor", units = "deg")
""" This is the window in which the entire experiment will take place. """
#help(mywin)
#Create stimulus

"""These are the general stimuli that the experiment will contain"""

#Introduction text
introduction_txt = visual.TextStim(win = mywin, text= "Hello! Welcome to the experiment. Press space to continue")
introduction_txt.draw()
mywin.flip()
while True:
        keys = kb.getKeys()
        if "space" in keys:
            break

explanation_txt = visual.TextStim(win = mywin, text = """In this simple visual reaction task, you will have to repeatedly distinguish between two pictures
Both pictures will show the same motive but one of them will be in a lower resolution than the other.
Your task will be to recognize the LOWER resolution picture as quickly as possible.
Press space to continue""")
explanation_txt.draw()
mywin.flip()
while True:
        keys = kb.getKeys()
        if "space" in keys:
            break

start_txt = visual.TextStim(win = mywin, text = """You can confirm your choice by pressing one of two buttons.
Press "f" if you think the picture on the LEFT is in LOWER resolution.
Press "j" if you think the picture on the RIGHT is in LOWER resolution.
Please try to react as quickly and as correctly as possible.
Press space to begin.""")
start_txt.draw()
mywin.flip()
while True:
        keys = kb.getKeys()
        if "space" in keys:
            break

#Trials                       
def trial():
    picture_1 = random.choice(image_list)
    picture_2 = random.choice(image_list)
    left = visual.ImageStim(win=mywin,image= picture_1,size = (16, 12),pos=[-9,0],texRes = 1280,interpolate = True)
    right = visual.ImageStim(win=mywin,image= picture_1,size = (16, 12), pos=[9,0], texRes = 12)
    instruction = visual.TextStim(win = mywin, text = """Which picture is in lower resolution?
Press "f" for the left picture.
Press "j" for the right picture.""", pos = [0, 10], color = (1.0, 1.0))
    left.draw()
    right.draw()
    instruction.draw()
    mywin.flip()
    while True:
        keys = kb.getKeys()
        if "f" in keys:
            break
        elif "j" in keys:
            break

for i in range(20):
    trial()
    
mywin.close()
core.quit()


