import pygame
import os
from config import *

# Fontes
MENU_FONT = "soloist1"
# Imagens
PLAYER_IMG = "player"
PLATFORM = "platform"
INIT_PLAT = "init_plat"
E1 = "enemy1"
PUKE = "puke_e1"
SPIKE = "spike"
FLAG = "flag"
THSTARS = "3stars"
TWSTARS = "2stars"
OSTAR = "1star"
CHECK = "checkbox"
E_CHECK = "empty_checkbox"
# Sons
JUMP_SFX = "jump_sfx"
DEATH_SFX = "death_sfx"

def load_assets():
    assets = {}

    assets[MENU_FONT] = pygame.font.Font(os.path.join(FNT_DIR, "soloist1.ttf"), 40)

    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert()
    assets[PLAYER_IMG] = pygame.transform.scale(assets["player"], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLATFORM] = pygame.image.load(os.path.join(IMG_DIR, "ok_platform.png")).convert_alpha()
    assets[PLATFORM] = pygame.transform.scale(assets["platform"], (PLATFORM_WIDTH, PLATFORM_HEIGHT))
    assets[INIT_PLAT] = pygame.image.load(os.path.join(IMG_DIR, "init_plat.png")).convert()
    assets[INIT_PLAT] = pygame.transform.scale(assets["init_plat"], (800, 200))

    assets[JUMP_SFX] = pygame.mixer.Sound(os.path.join(SND_DIR, "jump_sfx.mp3"))
    assets[DEATH_SFX] = pygame.mixer.Sound(os.path.join(SND_DIR, "death_sfx.mp3"))
    pygame.mixer.Sound.set_volume(assets[DEATH_SFX], 5000.0)

    assets[E1] = pygame.image.load(os.path.join(IMG_DIR, "paragoomba.png")).convert_alpha()
    assets[E1] = pygame.transform.scale(assets["enemy1"], (ENEMY_1_WIDTH, ENEMY_1_HEIGHT))

    assets[PUKE] = pygame.image.load(os.path.join(IMG_DIR, "laserRed16.png")).convert()

    assets[SPIKE] = pygame.image.load(os.path.join(IMG_DIR, "ok_spike.png")).convert_alpha()
    assets[SPIKE] = pygame.transform.scale(assets["spike"], (100, 50))

    assets[FLAG] = pygame.image.load(os.path.join(IMG_DIR, "flag.png")).convert_alpha()
    assets[FLAG] = pygame.transform.scale(assets["flag"], (60, 70))

    assets[THSTARS] = pygame.image.load(os.path.join(IMG_DIR, "3stars.png")).convert()
    assets[TWSTARS] = pygame.image.load(os.path.join(IMG_DIR, "2stars.png")).convert_alpha()
    assets[OSTAR] = pygame.image.load(os.path.join(IMG_DIR, "1star.png")).convert_alpha()

    assets[CHECK] = pygame.image.load(os.path.join(IMG_DIR, "checkbox.png")).convert()
    assets[CHECK] = pygame.transform.scale(assets["checkbox"], (60, 70))
    assets[E_CHECK] = pygame.image.load(os.path.join(IMG_DIR, "empty_checkbox.png")).convert()
    assets[E_CHECK] = pygame.transform.scale(assets["empty_checkbox"], (60, 70))

    return assets