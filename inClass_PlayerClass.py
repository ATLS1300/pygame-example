'''
Player class

AUTHOR:
DATE

Demonstrates Player class, with key and mouse interactions.

1. Make a surface (suface can hold images) (buttonFace)
2. Make a box to hold the location & size info (pygame.Rect)
3. Draw button face (& text) onto window surface (blit) 
6. Functions created for drawing (show), and key interaction (key) - call in while loop

'''
import pygame
pygame.init()

# Window
w = 400
h = 400
win = pygame.display.set_mode((w, h))

magenta = (255,0,255) 

# make a rectangle Surface & add to window
class Player:
    def __init__(self,x=w/2,y=h/2):
        self.color = magenta
        self.w = 100 # box width
        self.h = 50 # box height
        self.x = x
        self.y = y - self.h/2
        self.draw = True # control drawing
        self.box = pygame.Rect(self.x,self.y,self.w,self.h)  # store location info for pygame

        self.face = pygame.Surface((self.w,self.h)) # create surface for drawing
        self.face.fill(self.color) # pink colored face

    def show(self):
        if (self.draw):
            win.blit(self.face,(self.x,self.y)) #adds face to window

    def click(self,event):
        '''detect click event'''
        if pygame.mouse.get_pressed()[0]: # detect which mouse button was clicked
            x,y = pygame.mouse.get_pos()
            if self.box.collidepoint(x,y):
                print("click") # check that the detection happens
    
    # key interaction
    def key(self, event):
        '''Controls key interaction for a surface. To be called in event for loop.
          event - pygame event (from for loop)
          surface - pygame surface to draw on (win, buttonFace, etc.)'''
        global x
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
              # left arrow box to left
                if (self.x>self.w):
                  self.x -= 5
            if (event.key == pygame.K_RIGHT):
                if (self.x<w):
                  self.x += 5

def main():
    '''runs the script'''
    player = Player(y=100) # first object from Button class
    
    running = True
    
    while running:
        win.fill((0,0,0))
        
        for event in pygame.event.get():
            # ========= Add events here ========= 
            player.click(event)
            player.key(event)
            
            if (event.type == pygame.QUIT):
                pygame.quit()

        # ========= Add draw tasks here ========= 
        player.show() 
        
        pygame.display.update()

#  ========= Runs the code: ========= 
main()