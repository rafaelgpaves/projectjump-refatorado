import pygame, random, math, sys
from config import *
from funcs import *
from menu import menu
from level1 import level1

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nice")

state = MENU
while state != QUIT:
    if state == MENU:
        state = menu(window)
    elif state == LEVEL1:
        state = level1(window)

pygame.quit()