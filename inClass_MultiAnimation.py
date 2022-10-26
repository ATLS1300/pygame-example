"""
Pygame Animation Example Code
ATLS 1300/5650

Author: Dr. Z
10/20

Animates two shapes moving at the same time
(Can be used to draw yin yang symbol)

There are 5 steps to this task:
    1 - Load - Line 35
    2 - Resize image - Line
    3 - Position - Line 51
    
    Inside while loop
    4 - Add to window surface - Line 65
    5 - Update window - Line 81

"""

import pygame, math
pygame.init() # initialize pygame managers

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # define window variable
pygame.display.set_caption("Multiple Image Animation") # uncomment & edit to caption the window

#======================== Variables & functions ===================================================
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)
BLUE = (20,50,255)
RED = (255,0,0)

def circlePath(x_C,y_C,angle):
    """Solves for location on circlar path, using angle
    Arguments:
        x (float/int) - center of circle, horizontal
        y (float/int) - center of circle, vertical
        angle (float/int) - angle used to calculate point on circle 
        """
    global size
    x = size * math.sin(math.radians(angle)) + x_C
    y = size * math.cos(math.radians(angle)) + y_C
    return x,y

#================================ Animation loop ===================================================
def main():
    global size
    
    running = True
    clock = pygame.time.Clock() # for framerate timing

    # Step 1: SET START POSITIONS
    angle = 0
    inc = 1 # rate of change of angle, degrees
    size = 50 # radius of circles
    phase = 180 # change start position on circle path
    color = BLUE # start color for animation
    palette = [RED, BLUE] # for toggle
    switch = True

    x_center = w/2 # location of circle path center, horizontal
    y_center = h/2 # location of circle path center, vertical

    while running:
        
        #================== Your animation tasks ================    
        # clear window (comment out to have trace behind animation)
        # win.fill(BLACK) # keep this line for speed

        # Step 2: CALC & INCRERMENT POSITION (example uses parametric)
        x,y = circlePath(x_center,y_center,angle)
        x2,y2 = circlePath(x_center,y_center,angle+phase)

    
        angle += inc
        # Step 3: DRAW SHAPES 
        pygame.draw.circle(win,WHITE,(x,y),size)
        pygame.draw.circle(win,color,(x,y),10)

        pygame.draw.circle(win,color,(x2,y2),size)
        pygame.draw.circle(win,WHITE,(x2,y2),10)


        #================== Interactioons ================
        # This loop allows windows when exit is clicked.
        # Do not change, remove or augment this loop...yet.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # stops animation
                #pygame.quit() # stops running code & closes window
            if event.type == pygame.MOUSEBUTTONDOWN:
                # has a mouse button been clicked?
                switch = not switch
                color = palette[not switch]
                # print(switch)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    switch = not switch
                    color = palette[not switch]
        
        #================== Animation control ===================
        # Step 4: UPDATE SURFACE
        pygame.display.update()
        
        clock.tick(30) # framerate in fps (30-60 is typical)

main()