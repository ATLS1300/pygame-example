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


#================================ Animation loop ===================================================
# start run function def here
running = True
clock = pygame.time.Clock() # for framerate timing



while running:
    #================== Your animation tasks ================
    # call functions, increment values
    
    
    # clear window (comment out to have trace behind animation)
    win.fill(BLACK)

   
    #================== Interactinos ================
    # This loop allows windows when exit is clicked.
    # Do not change, remove or augment this loop...yet.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # stops animation
            #pygame.quit() # stops running code & closes window
                
    # stop conditional would go here 

    
    #================== Animation control ===================
    pygame.display.update()
    clock.tick(30) # framerate in fps (30-60 is typical)

# pygame.display.quit() # uncomment to automatically close window at end of animation    
