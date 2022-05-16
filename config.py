from os import path

# Pastas onde estão os assets
IMG_DIR = path.join(path.dirname(__file__), "assets", "images") # Pasta de imagens
SND_DIR = path.join(path.dirname(__file__), "assets", "sounds") # Pasta de sons

# Dados gerais do jogo
WIDTH = 300    # Largura da tela
HEIGHT = 700   # Altura da tela
FPS = 60       # Frames por segundo

# Define tamanhos
PLAYER_WIDTH = 51
PLAYER_HEIGHT = 51

# Define cores
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados do jogo
INIT = 0
LEVEL1 = 1
QUIT = 2