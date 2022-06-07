# ===== Inicialização =====
# --- Importando e inicializando pacotes
import pygame, random, math, sys
from config import *
from funcs import *
from init_screen import init_screen
from menu import menu
from level1 import level1
from level2 import level2
from level3 import level3
from end_screen import game_over
 
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
        state = level1(window)[0]
        tempo = level1(window)[1]
        if state == END_SCREEN:
            state = game_over(window, level1, tempo)
    elif state == LEVEL2:
        state = level2(window)[0]
        if state == END_SCREEN:
            state = game_over(window, level2)
    elif state == LEVEL3:
        state = level3(window)[0]
        if state == END_SCREEN:
            state = game_over(window, level3)

# ===== Finalização =====
pygame.quit() # Função do pygame que finaliza os recursos inicializados