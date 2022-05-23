from os import path

# Pastas onde estão os assets
FNT_DIR = path.join(path.dirname(__file__), "assets", "fonts") # Pasta de fontes
IMG_DIR = path.join(path.dirname(__file__), "assets", "images") # Pasta de imagens
SND_DIR = path.join(path.dirname(__file__), "assets", "sounds") # Pasta de sons

# Dados gerais do jogo
WIDTH = 600    # Largura da tela
HEIGHT = 700   # Altura da tela
FPS = 45       # Frames por segundo

# Define tamanhos
PLAYER_WIDTH = 52
PLAYER_HEIGHT = 52
PLATFORM_WIDTH = 150
PLATFORM_HEIGHT = 100

# Tamanhos de botões
LEVEL_BUTTON_WIDTH = 100
LEVEL_BUTTON_HEIGHT = 50
LEVEL1_BUTTON_XPOS = 50
LEVEL1_BUTTON_YPOS = 200
LEVEL2_BUTTON_XPOS = 50
LEVEL2_BUTTON_YPOS = 300
LEVEL3_BUTTON_XPOS = 50
LEVEL3_BUTTON_YPOS = 400

# Define cores
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 0, 150)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (150, 150, 0)

# Quantidade de inimigos e outros
PLATFORM_NUMBER = 2

# Estados do jogo
INIT = 0
MENU = 1
LEVEL1 = 2
LEVEL2 = 3
LEVEL3 = 4
END_SCREEN = 5
QUIT = 6

# Background
background_color = (0, 0, 0)
background_polygon_color = (48, 48, 48)