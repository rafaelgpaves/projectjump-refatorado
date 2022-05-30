import pygame
import random
import time
from config import *
from funcs import *
from assets import MENU_FONT, load_assets

def init_screen(window):
    square_effects = []
    cube_scroll = 0
    clock = pygame.time.Clock()
    assets = load_assets()
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                state = MENU
                running = False
        
        window.fill(BLACK)
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

            """ pygame.time.delay(7)

            fadeout(600, 750, window)
            fadein(600, 750, window)

            window.fill(LIGHT_RED)

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
            
            pygame.time.delay(7)
            fadeout(600, 750, window) """

            pygame.display.update()

    
    return state