import pygame
from config import *
from assets import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PLAYER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT

        self.speedx = 7 # Velocidade horizontal do jogador
        self.GRAVITY = 0 # Gravidade (começa em 0)

        self.jumps = 0 # Variável que conta o numero de pulos que o jogador deu
        self.max_jumps = 2 # Número máximo de pulos que o jogador pode dar

        self.is_on_wall = False # Variável que é True se o jogador estiver em contato com a parede, mas não com o chão e False caso contrário
        self.is_grounded = True
        self.on_platform = False
        self.is_on_platform_right = False
        self.is_on_platform_left = False

        self.groups = groups
        self.assets = assets

    def update(self):

        if self.is_on_wall == False and self.is_on_platform_left == False and self.is_on_platform_right == False and self.on_platform == False:
            self.GRAVITY += 1

        self.rect.x += self.speedx
        self.rect.y += self.GRAVITY

        if (self.rect.right >= WIDTH or self.rect.left <= 0) and self.is_grounded == False:
            self.is_on_wall = True
        else:
            self.is_on_wall = False

        if self.is_on_wall == True or self.is_on_platform_left == True or self.is_on_platform_right == True:
            self.jumps = 0 # Resetando o numero de pulos
            self.GRAVITY = 5 # Menor gravidade para sensação de deslizamento

        if self.rect.bottom >= HEIGHT or self.on_platform == True:
            self.is_grounded = True
        else:
            self.is_grounded = False

        if self.is_grounded == True:
            self.jumps = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            if self.is_on_wall == False:
                self.speedx = -7
        if self.rect.left < 0:
            self.rect.left = 0
            if self.is_on_wall == False:
                self.speedx = 7
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.is_on_wall = False
            self.is_grounded = True

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PLATFORM]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2

        self.groups = groups
        self.assets = assets