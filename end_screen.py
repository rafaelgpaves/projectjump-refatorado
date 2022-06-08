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


        tempofoi = assets[MENU_FONT].render("Seu tempo foi:", True, (255, 255, 255))
        tempofoi_rect = tempofoi.get_rect()
        tempofoi_rect.center = (WIDTH / 2, HEIGHT / 2)
        tempofoi_rect.top = tempofoi_rect.top - 300
        window.blit(tempofoi, tempofoi_rect)

        tempotxt = assets[MENU_FONT].render(str(tempo), True, (255, 255, 255))
        tempotxt_rect = tempotxt.get_rect()
        tempotxt_rect.center = (WIDTH / 2, HEIGHT / 2)
        tempotxt_rect.top = tempotxt_rect.top - 250
        window.blit(tempotxt, tempotxt_rect)


        msm = tempo.split(":")
        if len(msm) <= 2:
            while len(msm) != 3:
                msm.insert(0, "00")
        minutos = msm[0]
        segundos = msm[1]

        three_stars = assets[THSTARS]
        two_stars = assets[TWSTARS]
        one_star = assets[OSTAR]
        if level == "level1":
            if int(segundos) < 45 and minutos == 0:
                window.blit(three_stars, (WIDTH / 2 - three_stars.get_width() / 2, HEIGHT / 2 - three_stars.get_height() / 2))
            elif int(segundos) < 59 and minutos == 0:
                window.blit(two_stars, (WIDTH / 2 - two_stars.get_width() / 2, HEIGHT / 2 - two_stars.get_height() / 2))
            elif minutos >= 1:
                window.blit(one_star, (WIDTH / 2 - one_star.get_width() / 2, HEIGHT / 2 - one_star.get_height() / 2))


        pygame.display.update()
    return state