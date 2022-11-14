# IMPORT
from psychopy import gui, visual, monitors, event, core, logging
import os
import numpy
import time
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
# directory stuff
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
# set up monitor and window
mon = monitors.Monitor('myMonitor', width=24.5, distance=60)
mon.setSizePix([1920,1080])
win = visual.Window(monitor=mon)
# record frames
win.recordFrameIntervals = True
# add 4ms tolerance to the monitors refresh rate
win.refreshThreshold = 1.0/60.0 + 0.004
# tell it to report warnings
logging.console.setLevel(logging.WARNING)

# define refresh rate, my monitor is 60Hz
refresh=1.0/60.0
# set durations of strimuli being presented
fix_dur = 0.5 #500 ms
image_dur = 1 #1s
text_dur = 0.8 #800 ms

#set frame counts, make them whhole numbers
fix_frames = int(fix_dur / refresh) 
image_frames = int(image_dur / refresh) 
text_frames = int(text_dur / refresh) 
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)


# define start text
my_text = visual.TextStim(win)
strt_msg = "Hello, Press any key to begin"
strt_text = visual.TextStim(win, text=strt_msg)
#-define block (start)/end text using psychopy functions
blockstart = "Press any key to continue"
block_text = visual.TextStim(win, text=blockstart)
end_msg = "You've completed this trial"
end_text = visual.TextStim(win, text=end_msg)
#-define stimuli using psychopy functions (images, fixation cross)
cross = "+"
fx_cross = visual.TextStim(win, text=cross)
my_image = visual.ImageStim(win)

# making a list of the names of the stimuli
nums = []
for i in range(10) : 
    nums.append(i+1)
pics = ["face" + (str(i).zfill(2)) + ".jpg" for i in nums]
# set block + trial quantity
nBlocks=2
nTrials=3


#=====================
#START EXPERIMENT
#=====================
#-present start message text
strt_text.draw()
win.flip() 
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    block_text.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here
    numpy.random.shuffle(pics)

    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        # join the path of images with the names of the files
        # iterate pics list with current trial number
        my_image.image = os.path.join(image_dir,pics[trial])
        #=====================
        #START TRIAL
        #=====================  
        
        # for loop to draw the fixation cross for the prev specified 500ms
        for frameN in range(total_frames) :
            if 0 <= frameN <= fix_frames: # only runs if current frameN is within bounds of the fixation cross frame limits
                #-draw fixation
                fx_cross.draw()
                #-flip window
                win.flip()
                
                if frameN == fix_frames:
                    print("End fixation cross frame =", frameN)
        
        # for loop to draw the fixation cross for the prev specified 1 sec
            if fix_frames < frameN <= (fix_frames+image_frames) :      
                #-draw image
                my_image.draw()
                #-flip window
                win.flip()
                
                if frameN == (fix_frames+image_frames):
                    print("End image frame =", frameN)
           # for loop to draw the fixation cross for the prev specified 800ms        
            if (fix_frames+image_frames) < frameN < total_frames :
                #-draw end trial text
                end_text.draw()
                #-flip window
                win.flip()
                
                if frameN == (total_frames-1) :
                    print("End text frame =", frameN)
        # print number of frames dropped in each trial
        print('Overall, %i frames were dropped.' % win.nDroppedFrames)
#======================
# END OF EXPERIMENT
#======================        
win.close()