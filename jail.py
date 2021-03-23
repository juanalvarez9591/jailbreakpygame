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
TIMERLIMIT = "60" # need to be a str

# Score stuff
SCORE = 0
ScoreMining = False 
ScorePace = {"Normal":5}
SCORELIMIT = 100

# Displaying text
def displayText(text, x, y, fonttype="Consolas", fontsize=30, fontcolor=(0,0,0)):
    pygame.font.init()
    myfont = pygame.font.SysFont(fonttype, fontsize)
    textsurface = myfont.render(text, False, fontcolor)
    screen.blit(textsurface,(x,y))

# Sprite class

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MySprite, self).__init__()
        self.images = []

        self.images.append(pygame.image.load('assets/policeone.png'))
        self.images.append(pygame.image.load('assets/policeonse.png'))

        self.spriteheight = 64
        self.spritewidth = 64

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(x, y, self.spriteheight, self.spritewidth)

        #self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.


    def update(self):
        print(self.index)

        self.index += dt*2 # Frame upgrade velocity
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]

SpriteObject = MySprite(500, 200)
SpriteGroup = pygame.sprite.Group(SpriteObject)

# Game over condition
def GameOver():
    if timer == TIMERLIMIT and SCORE < SCORELIMIT:
        displayText("GAME OVER!", 10, 10)
    elif SCORE >= SCORELIMIT:
        displayText("YOU WIN!", 10, 10)

# Fixing FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Fixing FPS
    dt = clock.tick(30)/1000.0

    # Refesh screen
    SpriteGroup.update()
    screen.fill((255, 255, 255))
    SpriteGroup.draw(screen)

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
        Timer = displayText(timer, HEIGHT/2, WIDTH/2)
    else: 
        GameOver()

    pygame.display.flip()

pygame.quit()