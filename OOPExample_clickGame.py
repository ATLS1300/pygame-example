'''
Example bubble object game.

Demonstrates:
    Bubble class using init method, interaction and animation methods
    Creating single object and using dot notation
    Creating objects in lists & using loops & dot notation
        Animating 
        End game (check all objects for some condition)
        
THIS CODE DOES NOT KEEP BUBBLES ON SCREEN.
    
Borrowing from this code requires citation. Adds to 20% borrrow limit.
Similar methods are avaialle in the OOP Snippet Repo for free (no citation, borrow limit).
        https://github.com/ATLS1300/OOP_Snippets
'''


import pygame
import random, time
pygame.init()

# globals
w = 600
h = 600
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("Click Game")

# set colors
start_bg = (249, 233, 236) # lavendar blush
end_bg = (29, 47, 111) # st patricks blue
press_btn = (248, 141, 173) # darker pink
start_btn = (250, 199, 72)

win.fill(start_bg) # set background color as light

class Bubble:
    def __init__(self, startPos=(0,0),size=30, color=(0,255,255),step=5):
        self.x,self.y=startPos
        self.size=size
        self.fillColor=color 
        self.lineColor = (27, 64, 121)
        self.box=pygame.Rect(startPos[0],startPos[1],size,size) # CIRCLE POSITION INFO
        
        self.draw = True # to toggle appearance of object (hide- False, show- True)
        self.step = step # movement size
        
    def forward(self):
        if self.draw:
            # if drawing is on...
            self.box.move(self.step,self.step)
            
            # Same as:
            # self.x += self.step
            # self.y += step.step
        
    def rw(self):
        '''Creates a random walk. Each time the method is called, moves shape a random amount,
        limited by self.step'''
        self.x += random.randint(-self.step,self.step) # random size of movement
        self.y += random.randint(-self.step,self.step) # random size of movement
        
        self.show() # draw shapes
        
            
    def show(self):
        '''DIFFERENT FROM CLASS. draws outlined circle by drawing 2 circles on top of each other'''
        if self.draw:
            # draw is on...
            pygame.draw.circle(win,self.lineColor,(self.x,self.y),self.size+2)
            self.box=pygame.draw.circle(win,self.fillColor,(self.x,self.y),self.size)
    
    def checkClick(self):
        '''Checks for left mouesclick event. Call inside of event for loop.'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                # check for left mouse button
                if self.box.collidepoint(x, y):
                    # if click is inside & hide circle
                    self.draw = False # then turn off drawing
                    # self.size = -2 # stop drawing circle
                    

# REACH GOAL
class Timer:
    def __init__(self,limit=60):
        self.limit = limit
        self.clock = pygame.time.Clock()
        self.start=pygame.time.get_ticks() # get starter tick with Timer instantiation
        
        self.timeLeft = self.countDown()
        
    def countDown(self):
        currTime=(self.start + pygame.time.get_ticks())/1000 #calculate how many seconds
        return int(self.limit - currTime) # returns whole second numbers

# ADD TO MANAGER CLASS (PC09)
def checkViz(bubList):
    """Checks to see if all the bubbles are visible.
    Arguments:
        bubList - a list of Bubble objects
    Returns a boolean - True if there are visible bubbles left, False if not."""
    global text
    for bub in bubList:
        if (bub.draw):
            # check if any circle has a radius (drawing is on)
            # stop checking rest of list by returning a value (exits function)
            return True
    else:
        text = "You Win!"
        # prints "you win" IF win condition happens
        # pygame.quit() # close window
        return False #set win variable to the output


# MAKE A LIST OF 3 BUBBLE OBJECTS (start with few!)
bubList = []
for i in range(3):
     bubList.append(Bubble([random.randint(0,w-20),random.randint(0,h-20)])) # place at a random location

# TIMER & START CONDITIONS SETUP     
timeLeft = 30 # amount of time in seconds to play the game
timer = Timer(timeLeft)
text = "Game Over!"
running = True

# NOT HOW TIMER IS USED IN WHILE LOOP
while timeLeft > 0 and running:
    
    win.fill(start_bg)
    
    timeLeft = timer.countDown() # COUNT DOWN TIMER
    # ========== ANIMATE MOVEMENT ===========
    for bub in bubList:
        bub.rw()
    
    # EVENT FOR LOOP    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # stops animation
            pygame.quit()
        for bub in bubList:
            bub.checkClick() # call click method for each bubble
    
    # ========== CHECK END GAME CONDITIONS ========== 
    # breakpoint()
    running = checkViz(bubList)


    
    pygame.display.update()
    timer.clock.tick(30)
         
print(text) # prints you lose after time runs out & while lopo stops
