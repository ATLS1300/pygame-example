'''
EXAMPLE CODE - Writing text

This script demonstrates how to write text to a surface using a function. You will have to us objects
and calsses for yor assignmnts gooing forward. Thre is a commented out version of the writeText method for you to see
organization.
'''
import pygame
pygame.init()

# window (a surface)
w = 400
h = 400
win = pygame.display.set_mode((w,h))

# a second surface
sw = 200 # surface width
sh = 70 # surface height
colorBox = pygame.Surface((sw,sh))
colorBox.fill((255,255,255)) # make box white


# text settings (good ideas for attributes)
text = "Hello, world!"
fontSize = 20  #use no smaller than 18

def writeText(text,surface,color=(0,0,0),x=50,y=50):
    '''Writes text to a surface. text should be string.'''
    font = pygame.font.SysFont("Arial", fontSize) # arguments: (fontName, size, bold=False, italic=False)
    text = font.render(text, 1, color) #overwrite text input to turn it into blit-able content
    surface.blit(text, (x, y)) # add text to button surface
    
running = True

# animation loop -- needed to keep window open
while running:
    win.fill((0,0,0))
    
    writeText(text,win,color=(255,255,255)) # writes white text to window
    
    writeText(text,colorBox) # writes text to box (surface)
    win.blit(colorBox,(100,100)) # add white box to window
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()

    pygame.display.update()

# Syntax, organization for use in class:
# def writeText(self,x=0,y=0,bold=True):
#     '''writes text to a surface. Edit this docstring when borrowing.
#     Attributes required:
#         self.text - string.
#         self.surface - pygame Surface
#         self.fontSize - int (no less than 18)'''
#     font = pygame.font.SysFont("Arial", self.fontSize, bold=bold) # arguments: (fontName, size, bold=False, italic=False)
#     text = font.render(self.text, 1, pygame.Color("Black")) #overwrite text input to turn it into blit-able content
#     self.surface.blit(text, (x, y)) # add text to button Face