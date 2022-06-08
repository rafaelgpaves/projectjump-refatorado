import pygame
import random
from config import *
from funcs import *
from assets import *

def game_over(window, level, tempo):
    background_color = (0, 0, 0)
    square_effects = []
    cube_scroll = 0

    clock = pygame.time.Clock()
    assets = load_assets()

    running = True
    while running:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                state = QUIT
                running = False
            if e.type == pygame.KEYDOWN:
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
                background_polygon_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                pygame.draw.polygon(window, background_polygon_color, points, 2)


        text = assets[MENU_FONT].render("Seu tempo foi: " + str(tempo), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        text_rect.top = text_rect.top - 100
        window.blit(text, text_rect)

        msm = tempo.split(":")
        if len(msm) <= 2:
            while len(msm) != 3:
                msm.insert(0, "00")
        minutos = msm[0]
        segundos = msm[1]


        pygame.display.update()
    return state