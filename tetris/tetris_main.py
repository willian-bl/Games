import pygame
from pygame.locals import *
from sys import exit

from global_vars import *
from colors import *
from shapes import *  # S, Z, I, O, J, L, T
from functions import *

# functions
# - rotating shape in main
# - setting up the main


# Iniciando Pygame
pygame.init()
pygame.font.init()

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_pice = get_shape()
    fall_time = 0
    
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()
    while run:  # Loop principal
        clock.tick(CLOCK_FPS)
        tela.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_SPACE:  # Gira a peça
                    current_piece.rotation += 1
                if event.key == pygame.K_a:  # Faz a peça se mover para a esquerda
                    current_piece.x -= 1
                if event.key == pygame.K_s:  # Faz a peça cair mais rápido
                    current_piece.y += 1
                if event.key == pygame.K_d:  # Faz a peça se mover para a direita
                    current_piece.x += 1

        grid = create_grid()
        draw_window(tela, grid)

        current_piece.y += 0.05

        pygame.draw.rect(tela, current_piece.color, (current_piece.x * BLOCK_SIZE + TOP_LEFT_X, current_piece.y * BLOCK_SIZE + TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()

def main_menu():
    main()

if __name__ == '__main__': # start game
    main_menu()
