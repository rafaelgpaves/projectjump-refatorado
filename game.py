# ===== Inicialização =====
# --- Importando e inicializando pacotes
"Importando pygame e niveis"
import pygame
from config import WIDTH, HEIGHT, INIT, MENU, LEVEL1, LEVEL2, LEVEL3, END_SCREEN, QUIT
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

STATE = INIT
while STATE != QUIT:
    if STATE == INIT:
        STATE = init_screen(window)
    if STATE == MENU:
        STATE, dificuldade = menu(window)
    elif STATE == LEVEL1:
        STATE, tempo, dificuldade = level1(window, dificuldade)
        if STATE == END_SCREEN:
            STATE = game_over(window, "level1", tempo, dificuldade)
    elif STATE == LEVEL2:
        STATE, tempo, dificuldade = level2(window, dificuldade)
        if STATE == END_SCREEN:
            STATE = game_over(window, "level2", tempo, dificuldade)
    elif STATE == LEVEL3:
        STATE, tempo, dificuldade = level3(window, dificuldade)
        if STATE == END_SCREEN:
            STATE = game_over(window, "level3", tempo, dificuldade)

# ===== Finalização =====
pygame.quit() # Função do pygame que finaliza os recursos inicializados
