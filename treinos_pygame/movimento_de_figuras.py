import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

LARGURA = 1250
ALTURA = 680
FPS = 60

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Testando o Pygame :D')


def main():
    x = randint(25, LARGURA - 25)
    y = randint(25, ALTURA - 25)
    a = randint(-30, 30)
    b = randint(-30, 30)
    m = n = o = 255
    # x = y = a = b = 0

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos_mouse = pygame.mouse.get_pos()
                x = pos_mouse[0]
                y = pos_mouse[1]
                a = randint(-30, 30)
                b = randint(-30, 30)
                m = randint(1, 255)
                n = randint(1, 255)
                o = randint(1, 255)

        TELA.fill((0, 0, 0))

        # pygame.draw.rect(TELA, (255, 255, 0), (x, y, 50, 50))
        # y += 20
        # if y > ALTURA:
        #     y = 0
        #     x += 50
        #     if x > LARGURA - 10:
        #         x = 0
        #
        # pygame.draw.rect(TELA, (0, 255, 255), (a, b, 100, 100))
        # a += 15
        # if a > LARGURA:
        #     a = 0
        #     b += 100
        #     if b >= ALTURA -50:
        #         b = 0


        pygame.draw.circle(TELA, (m, n, o), (x, y), 50)
        x += a
        y += b
        if x >= LARGURA - 25 or x <= 25:
            a *= -1
        if y >= ALTURA - 25 or y <= 25:
            b *= -1


        pygame.display.update()

if __name__ == '__main__':
    main()