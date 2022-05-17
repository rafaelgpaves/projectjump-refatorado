import pygame
from config import *
from assets import *
from classes import *

def level1(window):

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

        all_sprites.update()

        window.fill(WHITE)
        all_sprites.draw(window)

        pygame.display.update()

    return state