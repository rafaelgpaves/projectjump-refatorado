import pygame, math, random
import numpy as np

def gira(lines, angle, amount):
    new_lines = lines.copy()
    new_lines[0] += math.cos(math.radians(angle)) * amount
    new_lines[1] += math.sin(math.radians(angle)) * amount
    return new_lines

def draw_cubes(window, background_polygon_color, cube_scroll, square_effects):
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