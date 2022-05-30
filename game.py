# ===== Inicialização =====
# --- Importando e inicializando pacotes
import pygame, random, math, sys
from config import *
from funcs import *
from init_screen import init_screen
from menu import menu
from level1 import level1

pygame.init()
pygame.mixer.init()

# --- Gerando a tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Jump")

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    if state == MENU:
        state = menu(window)
    elif state == LEVEL1:
        state = level1(window)

# ===== Finalização =====
pygame.quit() # Função do pygame que finaliza os recursos inicializados