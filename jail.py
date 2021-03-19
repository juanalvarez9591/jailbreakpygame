import pygame
import time

pygame.init()

# Screen resolution
HEIGHT = 800
WIDTH = 600

screen = pygame.display.set_mode([HEIGHT, WIDTH])

# Timer things outside loop
startTime = time.time()
timer = "0" # logic license, so we can check if timer is != than x (x will be != 0 so it will fakely pass the first time) before defining x
TIMERLIMIT = "30" # need to be a str

# Score stuff
SCORE = 0
ScoreMining = False 
ScorePace = 0.0005

def displayText(text, x, y, fonttype="Consolas", fontsize=30, fontcolor=(0,0,0)):
    pygame.font.init()
    myfont = pygame.font.SysFont(fonttype, fontsize)
    textsurface = myfont.render(text, False, fontcolor)
    screen.blit(textsurface,(x,y))

def GameOver():
    if timer == TIMERLIMIT:
        displayText("GAME OVER!", 10, 10)
    else: pass

# Fixing FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Fixing FPS
    dt = clock.tick(30)

    # Refesh screen
    screen.fill((255, 255, 255))

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

    if ScoreMining == True:
        SCORE += ScorePace*dt
    # Timer
    if timer != TIMERLIMIT:
        timer = str(int(time.time() - startTime))
        Timer = displayText(timer, HEIGHT/2, WIDTH/2)
    else: 
        GameOver()

    pygame.display.flip()

pygame.quit()