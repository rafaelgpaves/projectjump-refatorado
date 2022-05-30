import pygame, math, os

def gira(lines, angle, amount):
    new_lines = lines.copy()
    new_lines[0] += math.cos(math.radians(angle)) * amount
    new_lines[1] += math.sin(math.radians(angle)) * amount
    return new_lines

def fadeout(width, height, window): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(300, 0):
        fade.set_alpha(alpha)
        window.blit(fade, (0,0))
        pygame.time.delay(5)

def fadein(width, height, window): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        window.blit(fade, (0,0))
        pygame.time.delay(5)
