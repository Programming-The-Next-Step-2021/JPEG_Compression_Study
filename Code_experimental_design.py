"""This package contains the code for the experimental design. It includes all trials step by step.
It only works if you combine it with the contents of the compression-code.py package (some of which are imported into this package)."""
from psychopy import visual, core, event


#Create a window
mywin = visual.Window([800,600], monitor = "testMonitor", units = "deg")
""" This is the window in which the entire experiment will take place """
help(mywin)
#Create stimulus
stimulus = visual.GratingStim(win=mywin, mask="circle", size = 0.5, pos=[0,0], sf=0, rgb=-1)
"""These are the general stimuli that the experiment will contain"""
#stimulus.draw()
#mywin.update()
#core.wait(3.0)
while True:
    stimulus.setPhase(0.05, "+")
    stimulus.draw()
    mywin.flip()

    if len(event.getKeys())>0:
        break
    event.clearEvents()


mywin.close()
core.quit()


