import pygame
from pygame.locals import *
from sys import exit
import os

from colors import *
from shapes import *  # S, Z, I, O, J, L, T
from functions import *

# creating the data structure for pieces
# setting up global vars
# functions
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

# Iniciando Pygame
pygame.init()
pygame.font.init()

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

class Piece(object):
    pass

def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()
    while True:  # Loop principal
        clock.tick(CLOCK_FPS)
        tela.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()

def main_menu():
    main()

if __name__ == '__main__': # start game
    main_menu()
