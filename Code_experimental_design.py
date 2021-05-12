#This is going to be the code for the Experimental design
from psychopy import visual, core, event


#Create a window
mywin = visual.Window([800,600], monitor = "testMonitor", units = "deg")
#Create stimulus
stimulus = visual.GratingStim(win=mywin, mask="circle", size = 0.5, pos=[0,0], sf=0, rgb=-1)
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


