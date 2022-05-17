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

        self.groups = groups
        self.assets = assets

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.GRAVITY

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.bottom >= HEIGHT:
            self.jumps = 0 # Resetando o numero de pulos que o jogador pode dar