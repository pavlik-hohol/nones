import pygame
from pygame.draw import *
from random import randint

pygame.init()
posx = 750
posy = 750

FPS = 50
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
x1, y1 = randint(0, posx), randint(0, posy)
r = 35
color = COLORS[randint(0, 5)]

clock = pygame.time.Clock()
finished = False
results = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        keys = pygame.KEYDOWN
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                event.pos1 = event.pos[0]
                event.pos2 = event.pos[1]
                if x - r <= event.pos1 <= x + r and y - r <= event.pos2 <= y + r and x1 - r <= event.pos1 <= x1 + r and y1 - r <= event.pos2 <= y1 + r:
                    pass
                else:
                    continue
                print("results")
                results += 1
        if x < posx and y < posy:
            x += 5
            y += 5
            if y >= posy:
                y = 0
                x = 0
            if x >= posx:
                x = 0
                y = 0
        if x1 < posx and y1 < posy:
            x1 += 5
            y1 -= 5
            if y1 >= posy:
                y1 = posy - 1
                x1 = 0
            if x1 >= posx:
                x1 = 0
                y1 = posy - 1




    pygame.display.update()
    scr.fill(BLACK)
    circle(scr, COLORS[randint(5, 5)], (x1, y1), r)
    circle(scr, color, (x, y), r)
pygame.quit()
