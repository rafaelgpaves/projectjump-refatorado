import pygame
from config import *
from assets import *
from classes import *

def level1(window):

    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_platforms = pygame.sprite.Group()
    groups = {}
    groups["all_sprites"] = all_sprites
    groups["all_platforms"] = all_platforms

    player = Player(groups, assets)
    all_sprites.add(player)

    for i in range(PLATFORM_NUMBER):
        platform = Platform(groups, assets)
        all_platforms.add(platform)
        all_sprites.add(platform)

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
                    if player.is_on_platform_left == True:
                        player.is_on_platform_left = False
                        player.speedx = -7
                    elif player.is_on_platform_right == True:
                        player.is_on_platform_right = False
                        player.speedx = 7
                    if player.jumps < player.max_jumps:
                        player.GRAVITY = -20
                        player.jumps += 1

        platform_collision = pygame.sprite.spritecollide(player, all_platforms, False, pygame.sprite.collide_mask)
        for hit in platform_collision:
            # if player.rect.right > hit.rect.left:
            #     player.rect.right = hit.rect.left
            #     player.is_on_platform_left = True
            #     player.GRAVITY = 5
            if player.rect.bottom > hit.rect.top:
                player.rect.bottom = hit.rect.top
                player.is_grounded = True
                player.jumps = 0
            elif player.rect.top < hit.rect.bottom:
                player.rect.top = hit.rect.bottom  
            # elif player.rect.left < hit.rect.right:
            #     player.rect.left = hit.rect.right
            #     player.is_on_platform_right = True
            #     player.GRAVITY = 5

        if player.is_grounded == False and player.is_on_wall == False and player.is_on_platform_right == False and player.is_on_platform_right == False:
            player.GRAVITY += 1

        all_sprites.update()

        window.fill(WHITE)
        all_sprites.draw(window)

        pygame.display.update()

    return state