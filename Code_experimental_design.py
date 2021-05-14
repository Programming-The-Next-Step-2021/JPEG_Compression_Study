"""This package contains the code for the experimental design. It includes all trials step by step.
It only works if you combine it with the contents of the compression-code.py package (some of which are imported into this package)."""
from psychopy import visual, core, event
from PIL import Image
import PIL
import os
import glob
import random

from Stock_files_library import image_list
import Compression_code

#Create a window
mywin = visual.Window([1200,900], monitor = "testMonitor", units = "deg")
""" This is the window in which the entire experiment will take place """
#help(mywin)
#Create stimulus

uncompressed = random.choice(image_list)
compressed = uncompressed

stimulus = visual.ImageStim(win=mywin,
                              image= uncompressed,
                              size = (16, 12),
                              pos=[-9,0],
                            texRes = 1280,
                            interpolate = True)
stimulus2 = visual.ImageStim(win=mywin,
                              image= compressed,
                              size = (16, 12), pos=[9,0],
                             texRes = 12)

"""These are the general stimuli that the experiment will contain"""
stimulus.draw()
stimulus2.draw()
mywin.flip()
core.wait(5.0)
#while True:
#    stimulus.setPhase(0.05, "+")
#    stimulus.draw()
#    mywin.flip()
#
#    if len(event.getKeys())>0:
#        break
#    event.clearEvents()


mywin.close()
core.quit()


