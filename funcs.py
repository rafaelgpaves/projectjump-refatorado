import pygame, math
import numpy as np

def gira(lines, angle, amount):
    new_lines = lines.copy()
    new_lines[0] += math.cos(math.radians(angle)) * amount
    new_lines[1] += math.sin(math.radians(angle)) * amount
    return new_lines

def fade_out(window, color, speed):
    for alpha in np.arange(0, 255, speed):
        window.fill((color[0], color[1], color[2], alpha))
        pygame.display.update()
        pygame.time.delay(1)

def fade_in(window, color, speed):
    for alpha in np.arange(255, 0, -speed):
        window.fill((color[0], color[1], color[2], alpha))
        pygame.display.update()
        pygame.time.delay(1)