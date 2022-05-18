import pygame, math, random
from config import *
from assets import *
from classes import *
from funcs import *

window = pygame.display.set_mode((WIDTH, HEIGHT))
square_effects = []
player_pos = [window.get_width() // 2, window.get_height() // 2]

def level1(window):
    scrolling = 0
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups["all_sprites"] = all_sprites

    player = Player(groups, assets)
    all_sprites.add(player)

    keys_down = {}

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_SPACE:
                    if player.is_on_wall == True:
                        player.is_on_wall = False
                        if player.rect.right >= WIDTH:
                            player.speedx = -7
                        elif player.rect.left <= 0:
                            player.speedx = 7
                    if player.jumps < player.max_jumps:
                        player.GRAVITY = -20
                        player.jumps += 1

        if player.is_on_wall == False:
            player.GRAVITY += 1
        
        if scrolling < player_pos[1] - 200:
            scrolling += (player_pos[1] - 200 - scrolling) / 10

        all_sprites.update()

        window.fill((background_color))

        if random.randint(1, 60) == 1:
            square_effects.append([[random.randint(0, window.get_width()), -80 + scrolling], random.randint(0, 359), random.randint(10, 30) / 20, random.randint(15, 40), random.randint(10, 30) / 500])

        for i, effect in sorted(enumerate(square_effects), reverse = True):
            effect[0][1] += effect[2]
            effect[1] += effect[2] * effect[4]
            effect[3] -= effect[4]
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
       
        all_sprites.draw(window)

        pygame.display.update()

    return state