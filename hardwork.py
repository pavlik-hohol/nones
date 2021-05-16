import pygame
from pygame.draw import *
from random import randint

pygame.init()
posx = 750
posy = 750

FPS = 75
scr = pygame.display.set_mode((posx, posy))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = randint(0, posx)
y = randint(0, posy)
r = 20
color = COLORS[randint(0, 5)]

clock = pygame.time.Clock()
finished = False
results = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            y -= 20
        elif keys[pygame.K_DOWN]:
            y += 20
        elif keys[pygame.K_LEFT]:
            x -= 20
        elif keys[pygame.K_RIGHT]:
            x += 20
    pygame.display.update()
    scr.fill(BLACK)
    circle(scr, color, (x, y,), r)

pygame.quit()
