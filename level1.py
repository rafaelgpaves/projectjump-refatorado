import pygame, math, random
from config import *
from assets import *
from classes import *
from funcs import *

window = pygame.display.set_mode((WIDTH, HEIGHT))
square_effects = []

def level1(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    background = pygame.image.load("assets/images/background2.png")

    all_sprites = pygame.sprite.Group()
    all_platforms = pygame.sprite.Group()
    groups = {}
    groups["all_sprites"] = all_sprites
    groups["all_platforms"] = all_platforms

    player = Player(groups, assets)
    all_sprites.add(player)
    cube_scroll = 0

    for i in range(PLATFORM_NUMBER):
        platform = Platform(groups, assets, random.randint(PLATFORM_WIDTH, WIDTH-PLATFORM_WIDTH), random.randint(0, HEIGHT-PLATFORM_HEIGHT))
        all_platforms.add(platform)
        all_sprites.add(platform)

    keys_down = {}

    running = True
    while running:
        window.blit(background, (0, 0))
        clock.tick(FPS)

        for event in pygame.event.get():

            # Sair do jogo
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                # Pular
                if event.key == pygame.K_SPACE and player.jumps < player.max_jumps:
                    if player.is_on_wall == True: # Jogador está na parede
                        player.is_on_wall = False
                        if player.rect.right >= WIDTH:
                            player.speedx = -7
                        elif player.rect.left <= 0:
                            player.speedx = 7
                    if player.is_on_platform_left == True: # Jogador está no lado esquerdo da plataforma
                        player.is_on_platform_left = False
                        player.speedx = -7
                    elif player.is_on_platform_right == True: # Jogador está no lado direito da plataforma
                        player.is_on_platform_right = False
                        player.speedx = 7

                    player.GRAVITY = -20 # Diminuir a gravidade é o que faz o jogador ir para cima
                    player.jumps += 1
                    assets[JUMP_SFX].play()

        all_sprites.update()

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

        # Cronometro
        font_timer = pygame.font.Font(None, 36) # Fonte para escrever o timer
        passed_time = pygame.time.get_ticks() # Variável que guarda o tempo que passou desde o começo do nível
        seconds = passed_time // 1000 # Variável que guarda os segundos
        if seconds >= 60:
            seconds = seconds - 60*(minutes)
        minutes = passed_time // 60000 # Variável que guarda os minutos
        tempo = "{0}:{1}.{2}".format(minutes, seconds, str(passed_time)[-3:])
        timer = font_timer.render(tempo, True, WHITE)
        window.blit(timer, (WIDTH/2, 25))
       
        all_sprites.draw(window)

        pygame.display.update()

    return state