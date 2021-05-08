import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
scr = pygame.display.set_mode((750, 750))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """рисует новый шар"""
    global x, y, r
    x = randint(100, 750)
    y = randint(100, 750)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(scr, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
results = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos1, pos2 = pygame.mouse.get_pos()
            if (pos1 >= x - r) and (pos1 <= x + r) and (pos2 >= y - r) and (pos2 <= y + r):
                results += 1
                print(results)
                if results >= 50:
                    FPS = 2
                elif results == 30:
                    print("Через 20 очков скорость поднимится в два раза")
                    pygame.time.wait(200)
    new_ball()
    pygame.display.update()
    scr.fill(BLACK)

pygame.quit()
