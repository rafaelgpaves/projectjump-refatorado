import pygame, math, random
from config import *
from assets import *
from classes import *
from funcs import *

window = pygame.display.set_mode((WIDTH, HEIGHT))
square_effects = []

def level1(window):
    clock = pygame.time.Clock()

    total_time = pygame.time.get_ticks() # Variável que guarda o tempo total desde que o jogo foi iniciado

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_platforms = pygame.sprite.Group()
    #all_enemies = pygame.sprite.Group()
    all_spikes = pygame.sprite.Group()

    groups = {}
    groups["all_sprites"] = all_sprites
    groups["all_platforms"] = all_platforms
    #groups["all_enemies"] = all_enemies
    groups["all_spikes"] = all_spikes

    background = pygame.image.load("assets/images/background.png")
    bg = Background(background)
    # all_sprites.add(bg)

    player = Player(groups, assets)
    all_sprites.add(player)
    # player_bot = PlayerBottom(player.rect.bottom)

    cube_scroll = 0

    enemy1 = Enemy_1(groups, assets)
    all_sprites.add(enemy1)

    # Plataforma inicial (a mais de baixo)
    init_plat = Init_Platform(groups, assets, 0, HEIGHT)
    all_platforms.add(init_plat)
    all_sprites.add(init_plat)

    with open("plataformas1.txt", "r") as arquivo:
        plataformas = arquivo.readlines()
        print(plataformas)

    # Outras plataformas
    for i in range(len(plataformas)):
        # print(plataformas[i])
        plat = plataformas[i].split(",")
        # print(int(plat[0]))
        platform = Platform(groups, assets, int(plat[0]), int(plat[1]))
        all_platforms.add(platform)
        all_sprites.add(platform)

    # Espinhos
    for i in range(SPIKE_NUMBER):
        spike = Spike(groups, assets, 500, 400)
        all_spikes.add(spike)
        all_sprites.add(spike)

    keys_down = {}

    running = True
    while running:
        window.fill(BLACK)

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

                    player.GRAVITY = -15 # Diminuir a gravidade é o que faz o jogador ir para cima
                    player.jumps += 1
                    assets[JUMP_SFX].play()

                # Voltar ao menu
                if event.key == pygame.K_ESCAPE:
                    running = False
                    state = MENU
            
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

        all_sprites.draw(window)

        # Fazendo tudo se mover para baixo quando o jogador se aproxima do topo
        if player.rect.centery <= player.offset:
            if player.is_grounded == True or player.is_on_platform_left == True or player.is_on_platform_right == True or player.is_on_wall == True:
                continue
            else:
                player.rect.centery += abs(player.GRAVITY)
                # bg.rect.centery += abs(player.GRAVITY)
                for platform in all_platforms:
                    platform.rect.centery += abs(player.GRAVITY)
                for s in all_spikes:
                    s.rect.centery += abs(player.GRAVITY)

        if player.rect.bottom >= HEIGHT - player.offset:
            player.rect.centery -= abs(player.GRAVITY)
            for platform in all_platforms:
                platform.rect.centery -= abs(player.GRAVITY)
            for s in all_spikes:
                s.rect.centery -= abs(player.GRAVITY)

        # Checando colisão do jogador com espinhos
        spike_collision = pygame.sprite.spritecollide(player, groups["all_spikes"], False, pygame.sprite.collide_mask)
        if len(spike_collision) > 0:
            # player.rect.bottom = HEIGHT - 100
            # player.rect.centerx = WIDTH/2
            return LEVEL1

        # Cronômetro
        font_timer = pygame.font.Font(None, 36) # Fonte para escrever o timer
        passed_time = pygame.time.get_ticks() - total_time # Variável que guarda o tempo que passou desde o começo do nível
        seconds = passed_time // 1000 # Variável que guarda os segundos
        if seconds >= 60:
            seconds = seconds - 60*(minutes)
        minutes = passed_time // 60000 # Variável que guarda os minutos
        tempo = "{0}:{1}.{2}".format(minutes, seconds, str(passed_time)[-3:])
        timer = font_timer.render(tempo, True, WHITE)
        window.blit(timer, (WIDTH/2, 25))

        pygame.display.update()

    return state