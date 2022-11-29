"""
Pygame Image Example Code
ATLS 1300/5650

Author: Dr. Z
10/20

Sets Studio Ghibli scene as background.

There are 5 steps to this task:
    1 - Load - Line 35
    2 - Resize image - Line
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
w = 735
h = 405
win = pygame.display.set_mode((w,h)) # define window variable
pygame.display.set_caption("Background image") # uncomment & edit to caption the window

#======================== Variables & functions ===================================================
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)
YELLOW = (253, 208, 23)

# Step 1: LOAD IMAGE
# file must be in the same folder as script!
bckgnd = pygame.image.load("ghibliScene.jpg").convert() # convert() allows for faster drawing. USE IT!

# Step 2: RESIZE IMAGE
bckgnd = pygame.transform.scale(bckgnd,(w,h)) # Make same size as win
# note: I cahnged the window size to match the image
# when scaling, changind ratio (w:h) will distort image.

#================================ Animation loop ===================================================
# start run def here
running = True
clock = pygame.time.Clock() # for framerate timing

# Step 3: SET POSITION
x = 0 # image (start) location
y = 0

while running:
    
    #================== Your animation tasks ================
    # call functions, increment values
    
    # clear window (comment out to have trace behind animation)
    win.fill(BLACK) # keep this line for speed

    # Step 4: ADD IMAGE TO WINDOW SURFACE
    win.blit(bckgnd,(x,y)) # x,y is position of TOP LEFT CORNER
   
    # animate on top (uncomment to see)
    pygame.draw.circle(win,YELLOW,(w-100,100),50)
   
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
