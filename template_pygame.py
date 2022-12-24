import pygame
from pygame.locals import *
from sys import exit
import colors
import os

root = os.path.dirname(__file__)   
# config_ini = os.path.join(root, 'arquivos/nome_arquivo.wav')

# Iniciando Pygame
pygame.init()

LARGURA = 980
ALTURA = 550
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
while True:  # Loop principal
    clock.tick(FPS)
    tela.fill(colors.black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()