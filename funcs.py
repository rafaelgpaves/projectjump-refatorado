import math

def gira(lines, angle, amount):
    new_lines = lines.copy()
    new_lines[0] += math.cos(math.radians(angle)) * amount
    new_lines[1] += math.sin(math.radians(angle)) * amount
    return new_lines

def cronometro(passed_time):
    seconds = passed_time // 1000
    if seconds >= 60:
        seconds = seconds - 60*(minutes)
    minutes = passed_time // 60000
    tempo = "{0}:{1}.{2}".format(minutes, seconds, str(passed_time)[-3:])
    return tempo