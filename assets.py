import pygame
import os
from config import *

# Fontes
MENU_FONT = "soloist1"
# Imagens
PLAYER_IMG = "player"
PLATFORM = "platform"
INIT_PLAT = "init_plat"
E1_teste = "enemy1"
PUKE = "puke_e1"
SPIKE = "spike"
FLAG = "flag"

# Sons
JUMP_SFX = "jump_sfx"

def load_assets():
    assets = {}

    assets[MENU_FONT] = pygame.font.Font(os.path.join(FNT_DIR, "soloist1.ttf"), 40)

    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert()
    assets[PLAYER_IMG] = pygame.transform.scale(assets["player"], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLATFORM] = pygame.image.load(os.path.join(IMG_DIR, "platform.png")).convert()
    assets[PLATFORM] = pygame.transform.scale(assets["platform"], (PLATFORM_WIDTH, PLATFORM_HEIGHT))
    assets[INIT_PLAT] = pygame.image.load(os.path.join(IMG_DIR, "init_plat.png")).convert()
    assets[INIT_PLAT] = pygame.transform.scale(assets["init_plat"], (800, 200))

    assets[JUMP_SFX] = pygame.mixer.Sound(os.path.join(SND_DIR, "jump_sfx.mp3"))

    assets[E1_teste] = pygame.image.load(os.path.join(IMG_DIR, "e1_test.png")).convert()
    assets[E1_teste] = pygame.transform.scale(assets["enemy1"], (ENEMY_1_WIDTH, ENEMY_1_HEIGHT))

    assets[PUKE] = pygame.image.load(os.path.join(IMG_DIR, "laserRed16.png")).convert()

    assets[SPIKE] = pygame.image.load(os.path.join(IMG_DIR, "spike.png")).convert()
    assets[SPIKE] = pygame.transform.scale(assets["spike"], (100, 50))

    assets[FLAG] = pygame.image.load(os.path.join(IMG_DIR, "flag.png")).convert()

    return assets