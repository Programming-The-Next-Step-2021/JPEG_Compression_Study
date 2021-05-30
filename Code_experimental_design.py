"""This package contains the code for the experimental design. It includes all trials step by step.
It only works if you combine it with the contents of the compression-code.py package (some of which are imported into this package).
Also it is connected to the Stock files library, which contains all important images."""
from psychopy import visual, core, event, gui
from psychopy.hardware.keyboard import Keyboard
from psychopy.core import Clock, wait
from PIL import Image
import PIL
import os
import glob
import random
import numpy as np
import pandas as pd
from psychopy.gui import DlgFromDict


"""These are the imports from different files that connect to the experimental design.
The Stock_files_library file contains all the JPEG images in their original form.
In the Compression_code file, you can find the code in which the images are compressed."""
from Stock_files_library import image_list
from Compression_code import compression_trial, compressed_images, full_images, picture_sizes

#General issues
"""In this part, I create general objects that are necessary for the trials to function properly.
The clock object is used to measure participants reaction times later on.
The kb object is initialized to be able to collect participants keyboard responses.
The results object creates an excel sheet where all the different data is going to be exported to."""

clock = Clock()
kb = Keyboard()
results = pd.read_excel("/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Experimental_data.xlsx")


#Create a window
""" In this part, I create the window in which the entire experiment will take place.
The mywin object is a very basic window without many details."""

mywin = visual.Window([1200,900], monitor = "testMonitor", units = "deg")


#Dialogue window
"""In this part, I create a dialogue window that opens up at the beginning of the experiment.
The exp_info object asks for the participants initials, as well as for the last two letters of his mothers first name.
This way, the input will be used to assign each set of data to the correct participant, while the participant stays anonymus.
The dlg object initializes the dialogue window from the specific DlgFromDict python class.
The if statement ensures that the experiment will end automatically if the participant chooses to cancel it."""

exp_info = {'Enter your initials, followed by the last two letters of your mothers first name!': ''}
dlg = DlgFromDict(exp_info)
if not dlg.OK:
    print("Alright then, keep your secrets!")
    quit()


#Introduction text
"""In this part, I create the introduction text that welcomes the participant to the experiment.
The introduction_txt object initializes the text, that is then drawn to mywin.
The while statement makes sure, that you can enter the next page by pressing the Space key only."""

introduction_txt = visual.TextStim(win = mywin, text= "Hello! Welcome to the experiment. Press space to continue")
introduction_txt.draw()
mywin.flip()
while True:
        keys = kb.getKeys()
        if "space" in keys:
            break

#Explanation text
"""In this part, I initialize the text that explains the experimental design to the participants.
The explanation_txt object initializes the text, that is then drawn to mywin.
The while statement makes sure, that you can enter the next page by pressing the Space key only."""

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

#Start text
"""In this part, I initialize the last text, that participants see before starting the experiment.
The start_txt object explains the requested keyboard responses and how to quit the experiment. It is then drawn to mywin.
The while statement makes sure, that you can start the experiment by pressing the Space key only."""

start_txt = visual.TextStim(win = mywin, text = """You can confirm your choice by pressing one of two buttons.
Press "f" if you think the picture on the LEFT is in LOWER resolution.
Press "j" if you think the picture on the RIGHT is in LOWER resolution.
Please try to react as quickly and as correctly as possible.
You can always quit the experiment by pressing "q".
Press space to begin.""")
start_txt.draw()
mywin.flip()
while True:
        keys = kb.getKeys()
        if "space" in keys:
            break

#Starting the trials
"""This is where the fun begins! In this part, I initialize the trials that the experiment consists of. The idea is as followed:
Participants see two pictures at the same time on the screen. Both pictures show the same motive, but one of them is in lower resolution than the other one.
Participants then have to judge, which picture is in the lower resolution and have to press the corresponding key ("f" for left picture, "j" for right picture.
At each trial, the participants reaction time will be measured and saved to an excel data sheet.
The trial function initializes the whole trial design. All other objects will be explained step by step."""

#Initializing the trial
"""In this part, I initialize three lists in which data will be saved.
In the reaction_times list, all reaction times will be stored.
In the correct_images list, the correct image (the one with lower resolution) will be stored for each trial.
In the correct_key list, for each trial the key that represented the correct answer will be stored.
In the given_response list, each given key response will be stored.
"""

def trial():
    reaction_times = []
    correct_image = []
    correct_key = []
    given_response = []
    
    #Initialize the different stimuli
    """In this part, I initialize the stimuli that are going to appear on screen.
        The experiment will consist of 50 trials. The for loop initializes the number of trials, by using the range function.
        In the position_1 list, the position of the first stimulus is saved for all 50 trials. A 9 stands for it being placed on the right side, while a -9 stands for it being placed on the left side.
        In the position_2 list, the position of the second stimulus is saved for all 50 trials. The same settings apply as to the position_1 list.
        This is definitely not the most elegant solution, but it ensures that there are always two stimuli appearing on seperate sides of the screen in a "random" order.
        The fixation object stores a stimulus cross, that appears between each trial .
        The picture_1 object stores a jpeg image in its full size.
        The picture_2 object stores the same image but in a compressed state.
        The fullsize object makes picture_1 appear on the screen. The "pos" argument ensures that it appears either on the left or the right side of the screen.
        The compressed object makes picture_2 appear on the screen. The "pos" argument ensures that it appears either on the left or the right side of the screen.
        The instruction object makes a text appear above the two stimuli, which gives the instruction to press the corresponding key for the LOWER resolution image"""
    
    for i in range(5):
            position_1 = [-9,9,9,9,-9,9,-9,9,-9,9,-9,-9,9,9,9,9,-9,9,-9,9,-9,9,-9,-9,-9,9,-9,9,-9,9,-9,9,9,-9,-9,9,-9,9,-9,9,-9,9,-9,9,9,-9,-9,-9,-9,9]
            position_2 = [9,-9,-9,-9,9,-9,9,-9,9,-9,9,9,-9,-9,-9,-9,9,-9,9,-9,9,-9,9,9,9,-9,9,-9,9,-9,9,-9,-9,9,9,-9,9,-9,9,-9,9,-9,9,-9,-9,9,9,9,9,-9]
            fixation = visual.TextStim(win = mywin, text = "+")
            picture_1 = full_images[i]
            picture_2 = compressed_images[i]
            fullsize = visual.ImageStim(win=mywin,image= picture_1,size = (16, 12),pos=[position_1[i],0],texRes = 1280,interpolate = True)
            compressed = visual.ImageStim(win=mywin,image= picture_2,size = (16, 12), pos=[position_2[i],0], texRes = 12)
            instruction = visual.TextStim(win = mywin, text = """Which picture is in LOWER resolution?
Press "f" for the LEFT picture.
Press "j" for the RIGHT picture.""", pos = [0, 10], color = (1.0, 1.0))
            if position_2[i] == 9:
                    correct_key.append("j")
            elif position_2[i] == -9:
                    correct_key.append("f")
            
            
            #Draw stuff to the screen
            """In this part, all the prior defined stimuli are drawn to the screen.
                First, the fixation cross is drawn to the screen for 1 second (as initialized by the core.wait function.)
                Afterwards, both the fullsize and the compressed picture are drawn to the screen."""
            
            fixation.draw()
            mywin.flip()
            core.wait(1)
            fullsize.draw()
            compressed.draw()
            instruction.draw()
            mywin.flip()
            
            #Request keyboard response
            """In this part, I initialize the keyboard responses necessary for completing the different trials. Also I initialize the measurement of the reaction times for each response.
                The Clock.reset function ensures that the clock is set to zero before each keyboard response.
                The t_before object measures the time before the keyboard response but it will always be 0.
                The while loop makes sure, that you can only press three different keys to advance in each trial.
                When pressing the "f" or the "j" key, thee next trial will appear, initialized by the break function.
                Also the key that was pressed will be added to the given_response list, using the given_response.append function.
                When pressing the "q" key, the experiment will be aborted, initialized by the mywin.close and the core.quit function."""
            
            Clock.reset(clock)
            t_before = clock.getTime()
            while True:
                keys = kb.getKeys()
                if "f" in keys:
                    given_response.append("f")
                    break
                elif "j" in keys:
                    given_response.append("j")
                    break
                elif "q" in keys:
                    mywin.close()
                    core.quit()
                    
            #Measure keyboard responses and save data.
            """In this part, the keyboard responses are measured and saved to a datasheet.
            The t_after object gets the time after each keyboard response.
            The t_difference object calculates the difference between t_before and t_after and therefore calculates the reaction time for each keyboard response.
            In the reaction_times.append function, all reaction times will be added to the reaction_times list.
            In the correct_image.append function, for each trial the "correct" picture will be added to the correct_image list.
            The datasheet object creates a dataframe including the reaction_times, the correct_image, the correct_key, the given_response and the picture_size list.
            In the datasheet.to_excel function, the datasheet dataframe is exported to an excel sheet called Experimental_data.xlsx"""
                    
            t_after = clock.getTime()
            t_difference = t_after - t_before
            reaction_times.append(t_difference)
            correct_image.append(picture_2)
            datasheet = pd.DataFrame(list(zip(reaction_times, correct_image, correct_key, given_response, picture_sizes)),
               columns =['RT', 'Correct image', "Correct Response", "Given Response", "resolution"])
            datasheet.to_excel(excel_writer = "/Users/juliusmaerz/Documents/GitHub/Julius-Calendar_App/Experimental_data.xlsx",
                     index = False)


#Executing the trial function
"""In this part, the trial function is executed."""

trial()


#Ending Text
"""In this part, the end of the experiment is initialized.
The ending_txt object initializes a text that informs the participant that the experiment is now over and that he can close the window.
It is then drawn to mywin.
The while statement makes sure, that you can end the experiment by pressing the Space key only."""

ending_txt = visual.TextStim(win = mywin, text = """This is the end of the experiment. Thank you very much for participating.
Press space to close the window.""")
ending_txt.draw()
mywin.flip()
while True:
        keys = kb.getKeys()
        if "space" in keys:
            break


#Ending the experiment
"""In this part the end of the experiment is initialized.
The mywin.close function closes mywin and therefore the only window.
The core.quit function quits the experiment and stops the python code from running."""

mywin.close()
core.quit()


#EVTL: if list of compressed images == 9: correct key = j
#if list of compressed images = -9: correct key = f

