'''
Basic game demonstration built on code in class.

GAME DESCRIPTION:
Generates blue "friendly" balls that disappeear when clicked, and
red "enemy" balls that generate more balls when clicked. There is a 
chance that whenever a red ball is clicked, it may generate another red
ball too.
Click all the blue balls (ball.draw=False for all balls) to win.

MANAGER CLASS:
Uses Manager class to manage:
    - palette
    - object lists (enemy, ball)

The Manager class should:
    - run the main() method (minimum)
    - have lists of objects as attributes
    
The Manager class can also:
    - add objects to a list (listname.append(object))
    = remove objects fom a list (listname.remove(object))
    - check for game over conditions (all object.draw = False, all object.pos in range, etc.)
    - write game over text (text attribute, or object from another class)
    - have other game tools as objects:
        timer, score, lives, level
        
For levels (ADVANCED - grads and skilled coders only):
    - Do not do levels with multiple layouts/mazes, etc. 
    = Level changes mean: different palette (rest can beethe same), speed, number of enemeys, time to complete, etc.
    - add parameters to main() method (speed, palette, numEnemuy, etc)
    - update variables and attributes inside main() method accordingly.
    - generate a Button to call the main() method (with new arguments:
             self.main(speed[level],palette[level],numEnemy[level])
    - try for 1 level first.

'''

import pygame, random
pygame.init()

#Window
w = 750
h = 750
win = pygame.display.set_mode((w,h))

class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad = 50
        self.color = (24,120,233)
        self.draw = True # start with drawing on
        
        self.show() # draw a circle at instantiation
        
    def show(self):
        if (self.draw):
            self.box = pygame.draw.circle(win,self.color,(self.x,self.y), self.rad)
            # save Rect from circle to self.box
            
    def move(self,step=5):
        dx = random.randint(-step,step)
        dy = random.randint(-step,step)
        self.x += dx # updating the x position
        self.y += dy # updating the y position
        
        # edge conditionals
        
        self.show() # display on window 
        
    def key(self, event):
        '''Controls key interaction for a surface. To be called in event for loop.
        event - pygame event (from for loop)
        surface - pygame surface to draw on (win, buttonFace, etc.)'''
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
            # left arrow box to left
                if (self.x>self.rad):
                    self.x -= 1
                    print('left key press')
            if (event.key == pygame.K_RIGHT):
                if (self.x<w):
                    self.x += 5
                    print('right key press')  
            if (event.key == pygame.K_DOWN):
                if (self.y<h):
                    self.y += 5

            if (event.key == pygame.K_UP):
                if (self.y<h):
                    self.y -= 5    
    
    def click(self,event):
        '''Checks for click interaction inside Rect in class (self.box)
        
        Call inside event for loop
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                # check for left mouse button
                if self.box.collidepoint(x, y):
                    # check if click is inside & hide circle
                    self.draw = False
                    # self.size = -2 # stop drawing circle
               
    def collide(self,rect):
        if (self.box.colliderect(rect)):
            self.draw = False # turn off drawing
            print('hit')

class Enemy(Ball):
    '''Spawns more Balls and disappears when clicked.'''
    def __init__(self,x=w/2-100,y=h/2):
        super().__init__(x,y) #inherits all attributes & methods from superclass (Ball)
        self.color = (200,0,0) # all enemy balls are red
        self.clicked = False # click detection
        self.rad = 30 # make it smaller
        
    def click(self,event):
        '''Checks for click interaction inside Rect in class (self.box)
        
        Call inside event for loop
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            if pygame.mouse.get_pressed()[0]:
                # check for left mouse button
                if self.box.collidepoint(x, y):
                    
                    # check if click is inside & hide circle
                    self.clicked = True # change an attribute value
                    
                    self.draw = False # disappear when clicked.
                    # have the Manager monitor its state.
                                                
class Manager:
    '''class that runs the game
    attributes - specific to game (palette), lists of objects
    methods - main() method that executes game tasks'''
    def __init__(self):
        self.palette = [(24,120,233),(255,255,255),(0,0,50)]
        self.ballList = []
        self.numBall = 2
        self.enemy = Enemy() # makes 1 enemy

        for i in range(self.numBall):
            x = random.randint(0,w)
            y = random.randint(0,h)
            self.ballList.append(Ball(x,y))
    
    def checkClicked(self):
        '''any enemy objects have clicked=True
        if so, add more balls to the ball list.
        
        Uncomment lines for a random chance of adding more
        enemy balls'''
        if (self.enemy.clicked): 
            x = random.randint(0,w)
            y = random.randint(0,h)
            self.ballList.append(Ball(x,y))
            self.enemy.clicked = False # turn off to only make 1 enemy
            
            if (random.random()>0.5):
                # 50% chance of generating an Enemy object along with a Ball object 
                self.enemy = Enemy()
   
    def gameOver(self):
        '''check for end condition
        all balls in the list are inivisble (self.draw == False for all ball objects)'''  
        for ball in self.ballList:
            if (ball.draw):
                # any ball.draw is True  
                return False # stops the method and returns to main block of code
        # it finished the loop without any ball.draw being True
        return True   
    
    def main(self):
        running = True

        ball = Ball(w/2-100,h/2)
        
        # uncomment for collisions. Call collision() method in Ball
        # test = Ball(w/2,h/2)

        # test.color = self.palette[1]

        while running:
            win.fill(self.palette[2]) # clear the screen
            
            # test.show()
            self.enemy.move(7) # draw the enemy objects; they move faster
            
            for ball in self.ballList:
                ball.move()
            
            for event in pygame.event.get():
                for ball in self.ballList:

                    ball.key(event)
                    ball.click(event)
                    
                self.enemy.click(event) # calling the subclass method, which has 2 arguments
                
                self.checkClicked()           
                                             
                if (event.type == pygame.QUIT):
                    pygame.quit()
            
            if self.gameOver():
                '''if gameOver condition is met, True is returned'''
                print("You won!")
                running = False
                    
            pygame.display.update()
            
Manager().main()