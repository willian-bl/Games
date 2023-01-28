import pygame
from pygame.locals import *

from global_vars import *
from random import choice


# functions
# - create_grid
# - draw_grid
# - draw_window

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        shape_index = pieces['shapes'].index(shape)
        self.color = pieces['colors'][shape_index]
        self.rotation = 0


def create_grid(locked_positions={}):
    # Para relembrar: locked_position = dicionário {par (x,y) no grid : cor }
    grid = [[black for coluna in range(10)] for linha in range(20)]  # O espaço jogável do Tetris é uma grade retangular de 20 linhas x 10 colunas

    for linha in range(len(grid)):
        for coluna in range(len(grid[linha])):
            coord_grid = (coluna, linha)  # Usamos (coluna, linha) pois esse será meu par ordenado (x, y). Em termos de plano cartesiano, a coluna em que eu estou é determinada pelo valor no eixo x, já a linha pelo valor em y.
            if coord_grid in locked_positions:  # Se essa posição no grid já estiver ocupado, trocar para a cor da posição 
                cor = locked_positions(coord_grid)
                grid[linha, coluna] = cor

    return grid


def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape():
    random_shape = choice(pieces['shapes'])
    return Piece(5, 0, random_shape)


def draw_text_middle(text, size, color, surface):  
    pass
   

def draw_grid(surface, grid):
    for linha in range(len(grid)):
        for coluna in range(len(grid[linha])):
            x = TOP_LEFT_X + coluna * BLOCK_SIZE
            y = TOP_LEFT_Y + linha * BLOCK_SIZE
            grid_block = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, color=grid[linha][coluna], rect=grid_block, width=0)  #width=0 faz com que o retângulo não tenha nenhuma linha desenhada em suas bordas
    

def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def draw_window(surface:pygame.Surface, grid):
    surface.fill(black)

    font = pygame.font.SysFont('Verdana', 60)
    msg = font.render('Tetris', 1, white)
    surface.blit(msg, (TOP_LEFT_X + GRID_WIDTH/2 - msg.get_width()/2, 30))

    pygame.draw.rect(surface, white, (TOP_LEFT_X, TOP_LEFT_X, GRID_WIDTH, GRID_HEIGHT), 4)  # Desenhando o contorno da área jogável
    
    draw_grid(surface, grid)
    pygame.display.update()