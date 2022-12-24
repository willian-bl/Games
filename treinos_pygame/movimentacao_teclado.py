import pygame
from pygame.locals import *
from sys import exit

pygame.init()

LARGURA = 1250
ALTURA = 680
FPS = 60

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Testando o Pygame :D')


def main():
    VEL = 5
    x = LARGURA / 2 - 40
    y = ALTURA / 2 - 50

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        TELA.fill((0, 0, 0))


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:  # Esquerda
            x -= VEL
        if keys_pressed[pygame.K_d]:  # Direita
            x += VEL
        if keys_pressed[pygame.K_w]: # Cima
            y -= VEL
        if keys_pressed[pygame.K_s]:  # Baixo
            y += VEL

        pygame.draw.rect(TELA, (255, 255, 0), (x, y, 80, 100))

        pygame.display.update()


if __name__ == '__main__':
    main()
