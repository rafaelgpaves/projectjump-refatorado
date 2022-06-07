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
    all_enemies = pygame.sprite.Group()
    all_pukes = pygame.sprite.Group()
    all_spikes = pygame.sprite.Group()
    all_flags = pygame.sprite.Group()

    groups = {}
    groups["all_sprites"] = all_sprites
    groups["all_platforms"] = all_platforms
    groups["all_enemies"] = all_enemies
    groups["all_pukes"] = all_pukes
    groups["all_spikes"] = all_spikes
    groups["all_flags"] = all_flags

    background = pygame.image.load("assets/images/background.png")
    bg = Background(background)
    background_polygon_color = (48, 48, 48)
    # all_sprites.add(bg)

    cube_scroll = 0

    # Criando os inimigos

    for i in range(ENEMIES_NUMBER):
        ene_1 = Enemy_1(groups, assets, 0, HEIGHT)
        all_enemies.add(ene_1)
        all_sprites.add(ene_1)

    # Plataforma inicial (a mais de baixo)
    init_plat = Init_Platform(groups, assets, 0, INIT_PLAT_START_TOP)
    all_platforms.add(init_plat)
    all_sprites.add(init_plat)

    # Jogador
    player = Player(groups, assets, init_plat.rect.top)
    all_sprites.add(player)
    # player_bot = PlayerBottom(player.rect.bottom)

    # Abrindo o arquivo que possui as coordenadas de todas as plataformas do nível 1
    with open("plataformas1.txt", "r") as arquivo:
        plataformas = arquivo.readlines()

    # Outras plataformas
    for i in range(len(plataformas)):
        plat = plataformas[i].split(",")
        platform = Platform(groups, assets, int(plat[0]), int(plat[1]))
        all_platforms.add(platform)
        all_sprites.add(platform)
    
    # Abrindo o arquivo com as coordenadas dos inimigos do nível 1
    with open('posenem.txt', 'r') as arquivo:
        inimigo1 = arquivo.readlines()
    
    # Gerando os outros inimigos
    for i in range(len(inimigo1)):
        enem = inimigo1[i].split(',')
        enemy = Enemy_1(groups, assets, int(enem[0]), int(enem[1]))
        all_enemies.add(enemy)
        all_sprites.add(enemy)

    # Espinhos
    for i in range(SPIKE_NUMBER):
        spike = Spike(groups, assets, 530, -800)
        all_spikes.add(spike)
        all_sprites.add(spike)

    # Flag
    flag = Flag(groups, assets, HEIGHT/2, -4675)
    all_flags.add(flag)

    keys_down = {}

    running = True
    while running:
        window.fill((0, 0, 0))

        clock.tick(FPS)

        for event in pygame.event.get():

            # Sair do jogo
            if event.type == pygame.QUIT:
                running = False
                state = QUIT

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

        # Cubos!
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
        all_flags.draw(window)

        # Parte dos inimigos
        all_enemies.update()

        puke_hit = pygame.sprite.groupcollide(all_enemies, all_pukes, True, True, pygame.sprite.collide_mask) # (all_enemies, all_pukes, True, True, pygame.sprite.collide_mask)
        if len(puke_hit) > 0:
            # som da morte do jogador: assets['destroy_sound'].play()
            p = Player(assets, groups, init_plat.rect.top)
            all_sprites.add(p)
            #all_enemies.add(p)
            return LEVEL1
            
        enemy_hit = pygame.sprite.spritecollide(player, all_enemies, False, pygame.sprite.collide_mask)
        if len(enemy_hit) > 0:
            # adicionar parte de som
            # assets
            player.kill()
            # ao invés de explosion vai ser melt
            # sistema de derretimento do player
            # estado do derretimento (pygamev19)
            y_moved1 = INIT_PLAT_START_TOP - init_plat.rect.top - 300
            for platform in all_platforms:
                platform.rect.centery -= abs(y_moved1)
            for enemy in all_enemies:
                enemy.rect.centery -= abs(y_moved1)
            for s in all_spikes:
                s.rect.centery -= abs(y_moved1)
            player = Player(groups, assets, init_plat.rect.top)
            all_sprites.add(player)

        all_enemies.draw(window)

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
                flag.rect.centery += abs(player.GRAVITY)
                for enemy in all_enemies:
                    enemy.rect.centery += abs(player.GRAVITY)


        if player.rect.bottom >= HEIGHT - player.offset:
            player.rect.centery -= abs(player.GRAVITY)
            for platform in all_platforms:
                platform.rect.centery -= abs(player.GRAVITY)
            for s in all_spikes:
                s.rect.centery -= abs(player.GRAVITY)
            flag.rect.centery -= abs(player.GRAVITY)
            enemy.rect.centery -= abs(player.GRAVITY)

        # Checando colisão do jogador com espinhos
        spike_collision = pygame.sprite.spritecollide(player, groups["all_spikes"], False, pygame.sprite.collide_mask)
        if len(spike_collision) > 0:
            # player.rect.bottom = HEIGHT - 100
            # player.rect.centerx = WIDTH/2
            # return LEVEL1

            player.kill()

            # Movendo tudo para cima de novo
            y_moved = INIT_PLAT_START_TOP - init_plat.rect.top - 300
            for platform in all_platforms:
                platform.rect.centery -= abs(y_moved)
            for s in all_spikes:
                s.rect.centery -= abs(y_moved)
            player = Player(groups, assets, init_plat.rect.top)
            all_sprites.add(player)

        # Fim do level
        if len(pygame.sprite.spritecollide(player, groups["all_flags"], False, pygame.sprite.collide_mask)) > 0:
            running = False
            state = END_SCREEN
        
        # Cronômetro
        font_timer = pygame.font.Font(None, 36) # Fonte para escrever o timer
        passed_time = pygame.time.get_ticks() - total_time # Variável que guarda o tempo que passou desde o começo do nível
        seconds = passed_time // 1000 # Variável que guarda os segundos
        if seconds >= 60:
            seconds = seconds - 60*(int(minutes))
        minutes = passed_time // 60000 # Variável que guarda os minutos
        if seconds < 10:
            seconds = "0" + str(seconds)
        if minutes < 10:
            minutes = "0" + str(minutes)
        tempo = "{0}:{1}.{2}".format(minutes, seconds, str(passed_time)[-3:])
        timer = font_timer.render(tempo, True, WHITE)
        timer_rect = timer.get_rect()
        timer_rect.centerx = WIDTH/2
        timer_rect.top = 10
        window.blit(timer, timer_rect)

        pygame.display.update()

    return state, tempo