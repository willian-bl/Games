"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
import os
from colors import *
from shapes import *

# creating the data structure for pieces
# setting up global vars

# GLOBALS VARS
root = os.path.dirname(__file__)   
# musica = os.path.join(root, 'arquivos/nome_arquivo.wav')

LARGURA_TELA = 800
ALTURA_TELA = 700
GRID_WIDTH = 300  # meaning 300 // 10 = 30 width per block
GRID_HEIGHT = 600  # meaning 600 // 20 = 30 height per block
BLOCK_SIZE = 30
CLOCK_FPS = 60

TOP_LEFT_X = (LARGURA_TELA - GRID_WIDTH) // 2
TOP_LEFT_Y = ALTURA_TELA - GRID_HEIGHT

pieces = {'shapes': [S, Z, I, O, J, L, T],
          'colors': [green, red, cyan, yellow, orange, blue, purple]}
# index 0 - 6 represent shape