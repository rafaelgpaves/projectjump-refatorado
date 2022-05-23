import pygame
import os
from config import *

# Fontes
MENU_FONT = "VampireWars"
# Imagens
PLAYER_IMG = "player"
PLATFORM = "platform"
# Sons
JUMP_SFX = "jump_sfx"

def load_assets():
    assets = {}

    assets[MENU_FONT] = pygame.font.Font(os.path.join(FNT_DIR, "VampireWars.ttf"), 30)

    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert()
    assets[PLAYER_IMG] = pygame.transform.scale(assets["player"], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLATFORM] = pygame.image.load(os.path.join(IMG_DIR, "platform.png")).convert()
    assets[PLATFORM] = pygame.transform.scale(assets["platform"], (PLATFORM_WIDTH, PLATFORM_HEIGHT))

    assets[JUMP_SFX] = pygame.mixer.Sound(os.path.join(SND_DIR, "jump_sfx.mp3"))

    return assets