import pygame, random, math, sys
from config import *
from funcs import *
from level1 import level1

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nice")

state = LEVEL1
while state != QUIT:
    if state == LEVEL1:
        state = level1(window)

pygame.quit()

