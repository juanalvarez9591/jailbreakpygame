import pygame
import time

pygame.init()

# Screen resolution
HEIGHT = 800
WIDTH = 600

screen = pygame.display.set_mode([HEIGHT, WIDTH])

startTime = time.time()

def displayText(text, x, y, fonttype="Consolas", fontsize=30, fontcolor=(0,0,0)):
    pygame.font.init()
    myfont = pygame.font.SysFont(fonttype, fontsize)
    textsurface = myfont.render(text, False, fontcolor)
    screen.blit(textsurface,(x,y))


# Game loop
running = True
while running:
    screen.fill((255, 255, 255))

    timex = str(int(time.time() - startTime))
    displayText(timex, HEIGHT/2, WIDTH/2)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()