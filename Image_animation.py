"""
Pygame Image Example Code
ATLS 1300/5650

Author: Dr. Z
10/20

Draws, resizes, and rotates an Among Us character.

There are 5 steps:
    1 - Load - Line 35
    2 - Rotate - Line 42 
    3 - Position - Line 51
    
    Inside while loop
    4 - Add to window surface - Line 65
    5 - Update window - Line 81

For more image examples, check out Geeks4Geeks:
    https://www.geeksforgeeks.org/python-display-images-with-pygame/
    https://www.geeksforgeeks.org/how-to-rotate-and-scale-images-using-pygame/
"""

import pygame
pygame.init() # initialize pygame managers

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # define window variable
pygame.display.set_caption("Import image") # uncomment & edit to caption the window

#======================== Variables & functions ===================================================
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)

img_size = (400,400) # define img_size here for global access
angle = 90 # number of degreees to rotate image counter clockwise

# Step 1: LOAD IMAGES
# file must be in the same folder as script!
img = pygame.image.load("amongUsGreen.png").convert() # convert() allows for faster drawing. USE IT!
img = pygame.transform.scale(img,img_size)

# Step 2: ROTATE IMAGE (if desired)
img = pygame.transform.rotate(img,angle) # rotates image 90 degrees each time it's called
# when using in loop, note that each iteration will rotaate the image an 
# additional angle (90) degrees
#================================ Animation loop ===================================================
# start run def here
running = True
clock = pygame.time.Clock() # for framerate timing

# Step 3: SET POSITION
x = 0 # image (start) location
y = 0
inc = 0.5 # angle (for rotation)

while running:
    
    #================== Your animation tasks ================
    # call functions, increment values
    
    # clear window (comment out to have trace behind animation)
    win.fill(BLACK)

    # Step 4: ADD IMAGE TO WINDOW SURFACE
    win.blit(img,(x,y)) # x,y is position of TOP LEFT CORNER
   
    #================== Interactioons ================
    # This loop allows windows when exit is clicked.
    # Do not change, remove or augment this loop...yet.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # stops animation
            #pygame.quit() # stops running code & closes window
                    
    # stop conditional would go here too
    
    
    #================== Animation control ===================
    # Step 5: UPDATE SURFACE
    pygame.display.update()
    
    clock.tick(30) # framerate in fps (30-60 is typical)

# pygame.display.quit() # uncomment to automatically close window at end of animation    
