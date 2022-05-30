import pygame
from os import path
from config import *
from assets import MENU_FONT, load_assets

def init_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    running = True

    while running:
        clock.tick(FPS)