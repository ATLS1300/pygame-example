'''
Demonstrating animating multiple objects

AUTHOR: Dr. Z
DATE: 11/4

Objectives:
Rules:
Challenge:
Interaction:
'''
import pygame, random
pygame.init()

# Window object
w = 800
h = 600
win = pygame.display.set_mode((w, h))

# Clock object
clock = pygame.time.Clock() # found in PC06 start code

palette = [(255,0,255), (0,255,100), (0,255,255), (180,10,10)]
# magenta, teal, cyan, red

# make a rectangle Surface & add to window
class Bubble:
    def __init__(self):
        self.rad = 50 #radius
        self.x = random.randint(w/2,w-2*self.rad)
        diam = self.rad*2
        self.y = random.randint(h/2-self.rad*2, h-2*self.rad) # center 
        self.color = random.choice(palette) # start with green 
        self.draw = True # by default, draw shapes. Set to False to hide.
        
        self.vel_x = -5 # left velocity; step or inc variable equivalent
        
        self.box = pygame.draw.circle(win,self.color,(self.x,self.y),self.rad,0)  # store location info for pygame
        
    def show(self):
        '''draws our shapese onto the window (win)
        self.draw is like hide/show turtle'''
        if (self.draw):
            # only draw when self.draw is "on" (True)
            pygame.draw.circle(win,self.color,(self.box.x,self.box.y),self.rad,0)
            # to display, rely on pygame.display.update(), called in while loop

    def move(self):
        '''straight movement from right to left, wraps around when it leaves left side
        of screen and displays on screen'''
        self.box = self.box.move(self.vel_x,0) # over write self.box with new box from self.box.move method
        # move to the left horizontally, constant y.
        
        # CALL OTHER METHODS
        self.show() # CALL DRAWING METHOD IN MOVE(), FOR SLICKNESS
           
    def collide(self,rect):
        '''uses pygame collision to collide with another rect object.'''
        if (self.box.colliderect(rect)):
            self.draw = False # turn off drawing
        # if (self.box.collidepoint(x,y)): # for click collision
            
        
bubble = Bubble()
running = True

while running:
    win.fill((0,0,0)) # resetting background
    
    testRect = pygame.draw.rect(win,(255,255,255),(0,h/2,50,200)) # rect to collide with
    
    # CALL METHOD
    bubble.collide(testRect) # check for collision; pygame drawing methods return Rects. Handy!
    bubble.move() # delete this if you read comments.
    
    # Event for loop
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            
        # CALL METHOD
        if (bubble.x < -100):
            pygame.quit() # end demo if no collision
            
    pygame.display.update() # update the entire screen
    clock.tick(30) # clock tick call here, to control animation - argument = fps 
