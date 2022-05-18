import pygame
import os
from config import *

PLAYER_IMG = "player"
PLATFORM = "platform"

def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert()
    assets[PLAYER_IMG] = pygame.transform.scale(assets["player"], (PLAYER_WIDTH, PLAYER_HEIGHT))

    assets[PLATFORM] = pygame.image.load(os.path.join(IMG_DIR, "platform.png")).convert()
    assets[PLATFORM] = pygame.transform.scale(assets["platform"], (PLATFORM_WIDTH, PLATFORM_HEIGHT))
    
    return assets