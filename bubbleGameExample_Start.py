'''
Making an OOP game 
Examplifies building and using a Player class (controlled by used)

AUTHOR: Dr. Z
DATE: 11/4

Objective: 
        Match as many colors as possible before time runs out (30 or 15 s)
Rules: 
        1. Player can only move up and down, not left and right. 
        2. Bubbles only move left to right (maybe some wiggle to them?) # BUBBLES NOT CODED IN THIS SCRIPT
        3. Player can only disappear bubbles that match its color
        4. Player can’t touch top/bottom of screen or game over.

Challenge:
        1. If player collides with the wrong color, the square gets bigger, making it harder to avoid mismatching colored bubbles. (End game???)  # BUBBLES NOT CODED IN THIS SCRIPT
        2. Bigger size has a larger cost--can’t touch top/bottom of screen or game over.

Interaction:
        1. Bubbles don’t interact with each other, only the player
        2. Player can’t touch top or bottom screen edges or game over (edges have highlight?)

'''
import pygame
pygame.init()

# Window
w = 400
h = 400
win = pygame.display.set_mode((w, h))

palette = [(255,0,255), (0,0,0), (0,255,255), (180,10,10)]
# magenta, black, cyan, red

# make a rectangle Surface & add to window
class Player:
        
    '''Define Player class
    Define methods - no parameters (other than self)
        Move (to call in key and click methods)
        Click (interactions, use code from class)
'''
    def __init__(self):
        self.x = w-50
        self.y = h/2 # center
        self.w = 50
        self.h = 100
        self.color = (0,255,0) # start with green 
        self.draw = True # by default, draw shapes. Set to False to hide.
        
        self.box = pygame.Rect(self.x,self.y,self.w,self.h)  # store location info for pygame
        # Rect section inside documentions
        
        self.face = pygame.Surface((self.w,self.h)) # create surface for drawing
        self.face.fill(self.color) # pink colored face
        
    def show(self):
        '''draws our shapese onto the window (win)
        self.draw is like hide/show turtle'''
        if (self.draw):
            # only draw when self.draw is "on" (True)
            win.blit(self.face,(self.x,self.y)) 
            
    def key(self,event,up=pygame.K_w, down=pygame.K_s):
        '''Handles key interaction for a surface. To be called in event for loop.
            event - pygame event (from for loop)
            surface - pygame surface to draw on (win, buttonFace, etc.)'''
        if (event.type == pygame.KEYDOWN):
            if (event.key == up):
                # left arrow box to left
                if (self.y > self.w):
                    self.y -= 10
                    # print('left key press')
            if (event.key == down):
                if (self.y<w):
                    self.y += 10
        
square = Player() # instantiate Player object
square.draw = False # utrn off drawing of Player object
running = True

while running:
    win.fill((0,0,0))
    
    # Event for loop
    for event in pygame.event.get():
        # key press conditional
        square.key(event,down=pygame.K_x)
        # click conditional
        if (event.type == pygame.QUIT):
            pygame.quit()
            
    square.show() # adding the image to the screen Surface
    
    pygame.display.update() # update the entire screen
    # clock tick call here, to control animation 
