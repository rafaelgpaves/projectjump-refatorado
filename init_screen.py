import pygame
import random
import time
from config import *
from funcs import *
from assets import MENU_FONT, load_assets

def init_screen(window):
    # Tive que escrever de novo para não bugar o código
    background_color = (0, 0, 0)
    background_polygon_color = (48, 48, 48)
    square_effects = []
    cube_scroll = 0

    clock = pygame.time.Clock()
    assets = load_assets()
    
    running = True
    start_time = pygame.time.get_ticks()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                state = MENU
                running = False
        
        window.fill(background_color)
        if random.randint(1, 60) == 1:
            square_effects.append([[random.randint(0, window.get_width()), - 90 + cube_scroll], random.randint(0, 359), random.randint(10, 30) / 20, random.randint(15, 50), random.randint(10, 40) / 500])

        for i, effect in sorted(enumerate(square_effects), reverse = True):
            effect[0][1] += effect[2]
            effect[1] += effect[2] * effect[4]
            effect[3] -= effect[4] / 2
            points = [
                gira(effect[0], math.degrees(effect[1]), effect[3]),
                gira(effect[0], math.degrees(effect[1]) + 90, effect[3]),
                gira(effect[0], math.degrees(effect[1]) + 180, effect[3]),
                gira(effect[0], math.degrees(effect[1]) + 270, effect[3]),
            ]
            if effect[3] < 1:
                square_effects.pop(i)
            else:
                pygame.draw.polygon(window, background_polygon_color, points, 2)

            if pygame.time.get_ticks() - start_time > 7000:
                if background_color == (0, 0, 0):
                    background_color = (0, 51, 102)
                    background_polygon_color = (0, 128, 255)
                    start_time = pygame.time.get_ticks()
                elif background_color == (0, 51, 102):
                    background_color = (102, 0, 0)
                    background_polygon_color = (204, 0, 0)
                    start_time = pygame.time.get_ticks()
                elif background_color == (102, 0, 0):
                    background_color = (0, 0, 0)
                    background_polygon_color = (48, 48, 48)
                    start_time = pygame.time.get_ticks()

            title = assets[MENU_FONT].render("Project Jump", True, (255, 255, 255))
            title_rect = title.get_rect()
            title_rect.center = (window.get_width() / 2, window.get_height() / 2)
            window.blit(title, title_rect)

            ptp = assets[MENU_FONT].render("Pressione qualquer botão para jogar", True, (255, 255, 255))
            ptp = pygame.transform.scale(ptp, (200, 10))
            ptp_rect = ptp.get_rect()
            ptp_rect.center = (window.get_width() / 2, window.get_height() / 2 + 50)
            window.blit(ptp, ptp_rect)


        pygame.display.update()
    
    return state