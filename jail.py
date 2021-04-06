import pygame
import time
import math 
import random

pygame.init()

# Screen resolution
HEIGHT = 800
WIDTH = 600

screen = pygame.display.set_mode([HEIGHT, WIDTH])

# Timer things outside loop
startTime = time.time()
timer = "0" # logic license, so we can check if timer is != than x (x will be != 0 so it will fakely pass the first time) before defining x
TIMERLIMIT = "90" # need to be a str

# Score stuff
SCORE = 0
ScoreMining = False 
ScorePace = {"Normal":5, "Fast":10}
SCORELIMIT = 390
GameStop = False

# Displaying text
def displayText(text, x, y, fontsize=64, fontcolor=(0,0,0)):
    pygame.font.init()
    my_font = pygame.font.Font("assets/font.otf", fontsize) #Load font object.
    text = my_font.render(text, True, fontcolor) #Render text image.
    screen.blit(text, (x,y)) #Draw image to screen.

# Sprite classes 

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super(Sprite, self).__init__()
        self.images = []

        self.spriteheight = 0
        self.spritewidth = 0
        self.x = 1
        self.y = 1

        self.index = 0
        try:
            self.image = self.images[self.index]
            self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)
        except: pass

    def update(self):
        if GameStop != True:
            self.index += 0.2 # Frame upgrade velocity
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]

class Prisioner(Sprite):
    def __init__(self):
        super().__init__()
        self.idleprisioner = []
        self.hustlerprisioner = []
        for i in range(1,9):
            self.idleprisioner.append(pygame.image.load('assets/idleprisioner'+str(i)+'.png'))
        for i in range(1,17):
            self.hustlerprisioner.append(pygame.image.load('assets/hustlerprisoner'+str(i)+'.png'))

        self.x = 46
        self.y = 254
        self.spriteheight = 350
        self.spritewidth = 325
        self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)

        self.images = self.idleprisioner
    
    def update(self):
        super().update()
        if self.index % 2:
            if ScoreMining == False:
                self.images = self.idleprisioner
                self.x = 46
                self.y = 254
                self.spriteheight = 350
                self.spritewidth = 325
                self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)

            elif ScoreMining == True:
                self.images = self.hustlerprisioner
                self.x = 256
                self.y = 274
                self.spriteheight = 400
                self.spritewidth = 280
                self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)

class Police(Sprite):
    def __init__(self):
        super().__init__()
        self.yuta = []
        self.yutabusting = []
        self.yutaleft = [] 

        for i in range(1,5):
            self.yuta.append(pygame.image.load('assets/yuta'+str(i)+'.png'))
        for i in range(1,23):
            self.yutabusting.append(pygame.image.load('assets/yutahustling'+str(i)+'.png'))
        for i in self.yuta:
            self.yutaleft.append(pygame.transform.flip(i, True, False))

        self.images = self.yuta

        self.walkorientation = False
        self.walking = False
        self.busted = False
        self.x = 650
        self.y = 160
        self.spriteheight = 115
        self.spritewidth = 255
        self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)

    def update(self):
        super().update()
        print(self.x)
        if self.index % 2:
            if self.busted == False:
                if self.walking == True:
                    if self.x <= 105:
                        self.walkorientation = True
                    if self.x >= 610:
                        self.walkorientation = False
                        if random.randint(1,2) == 2:
                            self.walking = False

                    if self.walkorientation == False:
                        self.images = self.yuta
                        self.x -= 3
                        self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)
                    elif self.walkorientation == True:
                        self.images = self.yutaleft
                        self.x += 3
                        self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)

                elif self.walking == False:
                    self.x = 605
                    self.rect =  pygame.Rect(888, self.y, self.spriteheight, self.spritewidth)
                    if random.randint(1,75) == 1:
                        self.walking = True
            
            elif self.busted == True:
                self.images = self.yutabusting

            if self.x < 550 and ScoreMining == True:
                self.busted = True



# Calling sprites
PrisionerObject = Prisioner()
Prisioner = pygame.sprite.Group(PrisionerObject)

YutaObject = Police()
Yuta = pygame.sprite.Group(YutaObject)
# Progress bar setup
def ProgressBar():
    color = (255,0,0)
    pygame.draw.rect(screen, color, pygame.Rect(273, 75, int(SCORE), 100))

# Game over condition
def GameOver():
    global GameStop
    if timer == TIMERLIMIT:
        displayText("TIME'S UP!", 150, 175, 150, (225, 45, 44))
    elif SCORE >= SCORELIMIT:
        displayText("YOU WIN!", 200, 260, 150, (255, 165, 0))
        GameStop = True

# Fixing FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Fixing FPS TRY TO REMOVE IN FUTURE!
    dt = clock.tick(30)/1000.0

    # Refresh progress bar
    ProgressBar()

    # Refresh screen
    screen.blit(pygame.image.load('assets/background.png'), (0, 0))

    # Refresh police
    Yuta.update()
    Yuta.draw(screen)

    # Refresh cell
    screen.blit(pygame.image.load('assets/cell.png'), (0, 0))

    # Refresh prisioner sprite
    Prisioner.update()
    Prisioner.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ScoreMining = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            ScoreMining = False
    
    # Score handling
    displayText(str(int(SCORE)), 25, 25)

    if SCORE >= SCORELIMIT:
        ScoreMining = False
        GameOver()

    if ScoreMining == True:
        SCORE += ScorePace["Fast"]*dt

    # Timer
    if timer != TIMERLIMIT:
        timer = str(int(time.time() - startTime))
        Timer = displayText(timer, 150, 60)
    else: 
        GameOver()

    pygame.display.flip()

pygame.quit()