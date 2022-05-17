import pygame
import os
from config import *

PLAYER_IMG = "player"

def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert()
    assets[PLAYER_IMG] = pygame.transform.scale(assets["player"], (PLAYER_WIDTH, PLAYER_HEIGHT))
    return assets