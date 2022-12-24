import pygame
from pygame.locals import *
from sys import exit
from math import sqrt
import os

# Iniciando Pygame e variáveis
pygame.init()
pygame.mixer.init()

root = os.path.dirname(__file__)
aud_colisao = pygame.mixer.Sound(os.path.join(root, 'colisao_bolinha.wav'))

LARGURA = 500
ALTURA = 500
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('A ball')

branco = (255, 255, 255)
preto = (0, 0, 0)
bola_tam = 10
mouse_x = bola_x = LARGURA // 2 - bola_tam
mouse_y = bola_y = ALTURA // 2 - bola_tam

coordenadas = []
vel = 2
var_x = var_y = 0
aceleracao = -1/20
m = 25

clock = pygame.time.Clock()
while True:  # Loop principal
    clock.tick(FPS)
    tela.fill(preto)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:  # Quando solta o botão esquerdo do mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Grava a posição x e y do mouse
            delta_x = abs(mouse_x - bola_x)
            delta_y = abs(mouse_y - bola_y)
            dist = sqrt(delta_x**2 + delta_y**2)  # Distância entre o mouse e o centro da bolinha
            
            var_x = delta_x / dist  # Dividindo delta_x e delta_y em partes iguais e proporcionais ao tamanho da distância (hipotenusa)...
            var_y = delta_y / dist  # faz com que x e y variem proporcionalmente e mantenham a velocidade constante para qualquer dist, não importa o quão inclinada ou não seja a hipotenusa

            # Multiplica por -1 para mudar a direção. Esquerda/direita ou cima/baixo
            if bola_x < mouse_x:
                var_x *= -1
            if bola_y < mouse_y:
                var_y *= -1
            
            vel = dist / m # Velocidade que a bolinha anda de acordo com a força aplicada (varia de acordo com dist e a massa m da bolinha)
            print(vel)

            coordenadas = []  # Reseta a lista com coordenadas do rastro da bolinha

    if pygame.mouse.get_pressed()[0]:  # Se pressionar e segurar o botão esquerdo:
        mouse_linha = pygame.mouse.get_pos()  # Coordenada que o mouse está para desenhar a linha/calcular a distância da bolinha
        pygame.draw.line(tela, branco, (bola_x, bola_y), mouse_linha, 3)  # Linha da bolinha até o mouse
    
    # Faz o movimento da bolinha. Aqui a velocidade afeta seu movimento
    bola_x += var_x * vel
    bola_y += var_y * vel

    # Velocidade diminui com a aceleração negativa definida no início do código. Ou seja, a velocidade da bolinha diminui ao longo do tempo
    if vel > 0:
        vel += aceleracao
    else:
        vel = 0

    # A nova coordenada da bolinha, depois dela se movimentar, é colocada na lista de coordenadas para fazer o rastro 
    coordenadas.append((bola_x, bola_y))
    for ponto in coordenadas:  # Desenha o rastro da bolinha
        pygame.draw.circle(tela, (100, 100, 100), ponto, 1)
    
    # Se bater nos cantos, inverte x e/ou y
    if bola_x <= bola_tam or bola_x >= LARGURA - bola_tam:
        var_x *= -1
        aud_colisao.play()
    if bola_y <= bola_tam or bola_y >= ALTURA - bola_tam:
        var_y *= -1
        aud_colisao.play()
    
    pygame.draw.circle(tela, branco, (bola_x, bola_y), bola_tam)  # Desenha a bolinha

    pygame.display.update()
