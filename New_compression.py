from psychopy import visual, core, event
from PIL import Image
import PIL
import os
import sys
import glob
import random
from io import StringIO as BytesIO

from Stock_files_library import image_list
from io import BytesIO

def generate(self, image, format='jpeg'):
    im = random.choice(image_list)
    out = BytesIO()
    im.save(out, format=format,quality=75)
    out.seek(0)
    return out

