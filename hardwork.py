import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
scr = pygame.display.set_mode((1000, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]


def new_ball():
    """рисует новый шар"""
    global x, y, r
    x = randint(100, 1000)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(scr, color, (x, y), r)
    click(event)


def click(event):
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.MOUSEMOTION

            print("нажата,", pos)

    new_ball()
    pygame.display.update()
    scr.fill(BLACK)

pygame.quit()
