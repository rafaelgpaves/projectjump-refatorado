import math

def gira(lines, angle, amt):
    new_lines = lines.copy()
    new_lines[0] += math.cos(math.radians(angle)) * amt
    new_lines[1] += math.sin(math.radians(angle)) * amt
    return new_lines