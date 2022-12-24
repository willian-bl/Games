import pygame
from pygame.locals import *
from sys import exit
from math import sqrt

pygame.init()

LARGURA = 500
ALTURA = 500
FPS = 60

FONTE = pygame.font.SysFont('verdana', 20, False, False)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('A ball movement')

branco = (255, 255, 255)
preto = (0, 0, 0)
bola_tam = 10
mouse_x = bola_x = LARGURA // 2 - bola_tam
mouse_y = bola_y = ALTURA // 2 - bola_tam

coordenadas = []
vel = 5
# clicou = False
delta_x = delta_y = 0

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)

    tela.fill(preto)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_x = abs(mouse_x - bola_x)
            delta_y = abs(mouse_y - bola_y)
            dist = sqrt(delta_x**2 + delta_y**2)

    if bola_x < mouse_x:
        bola_x += delta_x * vel / dist 
    elif bola_x > mouse_x:
        bola_x -= delta_x * vel / dist

    if bola_y < mouse_y:
        bola_y += delta_y * vel / dist
    elif bola_y > mouse_y:
        bola_y -= delta_y * vel / dist

    coordenadas.append((bola_x, bola_y))
    for ponto in coordenadas:
        pygame.draw.circle(tela, (100, 100, 100), ponto, 1)

    pygame.draw.circle(tela, branco, (bola_x, bola_y), bola_tam)
    pygame.display.update()
