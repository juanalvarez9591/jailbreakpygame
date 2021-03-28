import pygame
import time
import math 

pygame.init()

# Screen resolution
HEIGHT = 800
WIDTH = 600

screen = pygame.display.set_mode([HEIGHT, WIDTH])

# Timer things outside loop
startTime = time.time()
timer = "0" # logic license, so we can check if timer is != than x (x will be != 0 so it will fakely pass the first time) before defining x
TIMERLIMIT = "10" # need to be a str

# Score stuff
SCORE = 0
ScoreMining = False 
ScorePace = {"Normal":5}
SCORELIMIT = 10

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
        self.index += 0.2 # Frame upgrade velocity
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]

class Prisioner(Sprite):
    def __init__(self):
        super().__init__()
        for i in range(1,9):
            self.images.append(pygame.image.load('assets/idleprisioner'+str(i)+'.png'))
        self.x = 46
        self.y = 254
        self.spriteheight = 255
        self.spritewidth = 115
        self.rect = pygame.Rect(self.x, self.y, self.spriteheight, self.spritewidth)

# Calling sprites
PrisionerObject = Prisioner()
Prisioner = pygame.sprite.Group(PrisionerObject)

# Game over condition
def GameOver():
    if timer == TIMERLIMIT and SCORE < SCORELIMIT:
        displayText("GAME OVER!", 150, 175, 150, (225, 45, 44))
    elif SCORE >= SCORELIMIT:
        displayText("YOU WIN!", 200, 260, 150, (255, 165, 0))

# Fixing FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # debugging mousepos
    mousex,mousey = pygame.mouse.get_pos()
    print(mousex, mousey)
    # Fixing FPS
    dt = clock.tick(30)/1000.0

    # Refesh screen
    screen.blit(pygame.image.load('assets/background.png'), (0, 0))
    
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
        SCORE += ScorePace["Normal"]*dt

    # Timer
    if timer != TIMERLIMIT:
        timer = str(int(time.time() - startTime))
        Timer = displayText(timer, 150, 60)
    else: 
        GameOver()

    pygame.display.flip()

pygame.quit()