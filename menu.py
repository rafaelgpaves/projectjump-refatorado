from os import path
import pygame
from config import SND_DIR, FPS, LEVEL1, LEVEL2, LEVEL3, QUIT, LEVEL_BUTTON_WIDTH, LEVEL_BUTTON_HEIGHT, LEVEL1_BUTTON_XPOS, LEVEL1_BUTTON_YPOS, LEVEL2_BUTTON_XPOS, LEVEL2_BUTTON_YPOS, LEVEL3_BUTTON_XPOS, LEVEL3_BUTTON_YPOS, GRAY, WHITE, DARK_GRAY, DARKEST_BLUE, DARK_BLUE, RED, LIGHT_RED, BLACK
from assets import CHECK, E_CHECK, MENU_FONT, load_assets

def menu(screen):

    clock = pygame.time.Clock()

    assets = load_assets()

    dificuldade = [True, True]
    # lista em que o primeiro elemento indica se os inimigos vão aparecer o segundo indica se os inimigos vão aparecer

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

                # Entrar no nível 1
                if inside_level_1 == True:
                    state = LEVEL1
                    running = False

                # Entrar no nível 2
                if inside_level_2 == True:
                    state = LEVEL2
                    running = False

                # Entrar no nível 3
                if inside_level_3 == True:
                    state = LEVEL3
                    running = False

                # Ativar/desativar inimigos
                if inside_enemy == True:
                    if dificuldade[0] == True:
                        dificuldade[0] = False
                    elif dificuldade[0] == False:
                        dificuldade[0] = True

                # Ativar/desativar espinhos
                if inside_spike == True:
                    if dificuldade[1] == True:
                        dificuldade[1] = False
                    elif dificuldade[1] == False:
                        dificuldade[1] = True

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

        # Botão de ativar/desativar inimigos
        inside_enemy = False # Variável que é True se o mouse estiver dentro da caixa e False caso contrário
        if dificuldade[0] == True: # Se os inimigos estiverem ativados, aparecerá um certinho
            screen.blit(assets[CHECK], (50, 550))
        elif dificuldade[0] == False: # Se os inimigos estiverem desativados, aparecerá um X
            screen.blit(assets[E_CHECK], (50, 550))
        enemy_text = assets[MENU_FONT].render("Inimigos", True, WHITE)
        screen.blit(enemy_text, (125, 560))
        if mouse[0] in range(50, 50 + 60) and mouse[1] in range(550, 550 + 70):
            inside_enemy = True

        # Botão de ativar/desativar espinhos
        inside_spike = False # Variável que é True se o mouse estiver dentro da caixa e False caso contrário
        if dificuldade[1] == True: # Se os espinhos estiverem ativados, aparecerá um certinho
            screen.blit(assets[CHECK], (50, 630))
        elif dificuldade[1] == False: # Se os espinhos estiverem desativados, aparecerá um X
            screen.blit(assets[E_CHECK], (50, 630))
        spikes_text = assets[MENU_FONT].render("Espinhos", True, WHITE)
        screen.blit(spikes_text, (125, 640))
        if mouse[0] in range(50, 50 + 60) and mouse[1] in range(630, 630 + 70):
            inside_spike = True

        # Invertendo o display
        pygame.display.flip()

    return state, dificuldade
