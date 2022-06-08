import pygame
from os import path
from config import *
from assets import MENU_FONT, load_assets

def menu(screen):

    clock = pygame.time.Clock()

    assets = load_assets()

    pygame.mixer.music.load((path.join(SND_DIR, "menu_music.mp3")))
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:

        # Ajustando a velocidade do jogo
        clock.tick(FPS)

        # Tratando os eventos
        for event in pygame.event.get():

            # Evento de sair
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            # Evento para começar o jogo
            if event.type == pygame.MOUSEBUTTONDOWN:

                if inside_level_1 == True:
                    state = LEVEL1
                    running = False

                if inside_level_2 == True:
                    state = LEVEL2
                    running = False

                if inside_level_3 == True:
                    state = LEVEL3
                    running = False

        # Pegando a posição do mouse (e colocando numa tupla)
        mouse = pygame.mouse.get_pos()

        # Desenhando a tela
        screen.fill(BLACK)

        # Botão para entrar no nível 1
        inside_level_1 = False # variável 'True' se o mouse estiver dentro do botao do Nível 1 e 'False' caso contrário
        pygame.draw.rect(screen, GRAY, (LEVEL1_BUTTON_XPOS, LEVEL1_BUTTON_YPOS, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT))
        LEVEL1_TEXT = assets[MENU_FONT].render("LEVEL 1", True, WHITE)
        screen.blit(LEVEL1_TEXT, (LEVEL1_BUTTON_XPOS + 7, LEVEL1_BUTTON_YPOS + 15))
        if mouse[0] in range(LEVEL1_BUTTON_XPOS, LEVEL1_BUTTON_XPOS + LEVEL_BUTTON_WIDTH) and mouse[1] in range(LEVEL1_BUTTON_YPOS, LEVEL1_BUTTON_YPOS + LEVEL_BUTTON_HEIGHT):
            inside_level_1 = True 
            pygame.draw.rect(screen, DARK_GRAY, (LEVEL1_BUTTON_XPOS, LEVEL1_BUTTON_YPOS, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT))
            LEVEL1_TEXT = assets[MENU_FONT].render("LEVEL 1", True, GRAY)
            screen.blit(LEVEL1_TEXT, (LEVEL1_BUTTON_XPOS + 7, LEVEL1_BUTTON_YPOS + 15))

        # Botão para entrar no nível 2
        inside_level_2 = False # variável 'True' se o mouse estiver dentro do botao do Nível 2 e 'False' caso contrário
        pygame.draw.rect(screen, DARK_BLUE, (LEVEL2_BUTTON_XPOS, LEVEL2_BUTTON_YPOS, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT))
        LEVEL2_TEXT = assets[MENU_FONT].render("LEVEL 2", True, WHITE)
        screen.blit(LEVEL2_TEXT, (LEVEL2_BUTTON_XPOS, LEVEL2_BUTTON_YPOS + 15))
        if mouse[0] in range(LEVEL2_BUTTON_XPOS, LEVEL2_BUTTON_XPOS + LEVEL_BUTTON_WIDTH) and mouse[1] in range(LEVEL2_BUTTON_YPOS, LEVEL2_BUTTON_YPOS + LEVEL_BUTTON_HEIGHT):
            inside_level_2 = True 
            pygame.draw.rect(screen, DARKEST_BLUE, (LEVEL2_BUTTON_XPOS, LEVEL2_BUTTON_YPOS, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT))
            LEVEL2_TEXT = assets[MENU_FONT].render("LEVEL 2", True, GRAY)
            screen.blit(LEVEL2_TEXT, (LEVEL2_BUTTON_XPOS, LEVEL2_BUTTON_YPOS + 15))

        # Botão para entrar no nível 3
        inside_level_3 = False # variável 'True' se o mouse estiver dentro do botao do Nível 3 e 'False' caso contrário
        pygame.draw.rect(screen, RED, (LEVEL3_BUTTON_XPOS, LEVEL3_BUTTON_YPOS, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT))
        LEVEL3_TEXT = assets[MENU_FONT].render("LEVEL 3", True, WHITE)
        screen.blit(LEVEL3_TEXT, (LEVEL3_BUTTON_XPOS, LEVEL3_BUTTON_YPOS + 15))
        if mouse[0] in range(LEVEL3_BUTTON_XPOS, LEVEL3_BUTTON_XPOS + LEVEL_BUTTON_WIDTH) and mouse[1] in range(LEVEL3_BUTTON_YPOS, LEVEL3_BUTTON_YPOS + LEVEL_BUTTON_HEIGHT):
            inside_level_3 = True 
            pygame.draw.rect(screen, LIGHT_RED, (LEVEL3_BUTTON_XPOS, LEVEL3_BUTTON_YPOS, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT))
            LEVEL3_TEXT = assets[MENU_FONT].render("LEVEL 3", True, GRAY)
            screen.blit(LEVEL3_TEXT, (LEVEL3_BUTTON_XPOS, LEVEL3_BUTTON_YPOS + 15))

        # Invertendo o display
        pygame.display.flip()

    return state