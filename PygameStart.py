"""
Pygame Startere Code
ATLS 1300/5650

Author: In Class
10/20

NOTE: the animation loop is inifinite. You will have to add a conditional
to break the loop, if desired. Infinite looping animation can be used intentionally!

Makes a white rectangle blink on a black background.
'''"""

import pygame
pygame.init() # initialize pygame managers

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # define window variable
# pygame.display.set_caption("Read carefully.") # uncomment & edit to caption the window

#======================== Variables & functions ===================================================
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)

def blinkBox(counter):
    # use modulo to occasionally draw a white box
    if (counter % 20)>9:
        pygame.draw.rect(win,WHITE,(x,y,size,size))

    counter += 1
    return counter

def blinkBoxGlobal():
    global counter
    local = "I'm local"
    # use modulo to occasionally draw a white box
    if (counter % 20)>9:
        pygame.draw.rect(win,WHITE,(x,y,size,size))

    counter += 1
#================================ Animation loop ===================================================
# start values defined here
running = True
clock = pygame.time.Clock() # for framerate timing

size = 200
y = h/2-size/2
switch = True
counter = 0

while running:
    # clear window (comment out to have trace behind animation)
    win.fill(BLACK)

    # counter = blinkBox(counter)
    blinkBoxGlobal()
    x = w/2-size/2 # center, adjusted for width of shape

    # # use modulo to occasionally draw a white box
    # if (counter % 20)>9:
    #     pygame.draw.rect(win,WHITE,(x,y,size,size))

    # counter += 1
   

    # This loop allows windows when exit is clicked.
    # Do not change, remove or augment this loop...yet.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # stops animation
            #pygame.quit() # stops running code & closes window
                
    #================== Your animation tasks ================
    # call functions, increment values
    
    # stop conditional would go here too
    
    
    #================== Animation control ===================
    pygame.display.update()
    clock.tick(30) # framerate in fps (30-60 is typical)

# pygame.display.quit() # uncomment to automatically close window at end of animation    