""" O objetivo desse código é recriar o famoso jogo da cobrinha, ou snake game, usando funções e lógica básica do pygame. """

#  ---------------- Imports --------------
import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os

#  ------------------- Iniciando o pygame e todas as bibliotecas que vou usar ------------------------------
pygame.init()
pygame.mixer.init()

#  ----------------- Cores RGB ----------------------
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

#  ----------------- Variáveis fixas -------------------------------
LARGURA = 480
ALTURA = 520

TELA = pygame.display.set_mode((LARGURA, ALTURA))

CLOCK = pygame.time.Clock()

aumentar_velocidade = True

TAMANHO_COBRA = 20
TAMANHO_MACA = 20

VEL = 20

FONTE_PONTOS = pygame.font.SysFont('verdana', 30, True, False)
FONTE_VELOCIDADE = pygame.font.SysFont('verdana', 20, False, False)
FONTE_GAMEOVER = pygame.font.SysFont('impact', 30, False, False)

# -------------------- Importando sons e imagens ----------------

root = os.path.dirname(__file__)

som_maca = pygame.mixer.Sound(os.path.join(root, 'arquivos/apple_pickup.wav'))
som_gameover = pygame.mixer.Sound(os.path.join(root, 'arquivos/death.wav'))
som_speedup = pygame.mixer.Sound(os.path.join(root, 'arquivos/speed_up.wav'))
musica_de_fundo = pygame.mixer.music.load(os.path.join(root, 'arquivos/Free 8-bit loop.wav'))
icone = pygame.image.load(os.path.join(root, 'arquivos/snake-icon.png'))

pygame.display.set_caption('Snake Game - Jogo da Cobrinha')
pygame.display.set_icon(icone)

#  -------------------- Definindo Funções -----------------------


def aumenta_cobra(lista_cobra):
    for posicao_cabeca in lista_cobra:
        pygame.draw.rect(TELA, VERDE, (posicao_cabeca[0], posicao_cabeca[1], TAMANHO_COBRA, TAMANHO_COBRA))


def game_over(pts):
    TELA.fill(BRANCO)

    mensagem_2 = f'Fim de jogo! Sua pontuação foi: {pts}'
    mensagem_3 = 'Pressione R para jogar novamente'
    texto_formatado_2 = FONTE_GAMEOVER.render(mensagem_2, True, PRETO)
    texto_formatado_3 = FONTE_GAMEOVER.render(mensagem_3, True, PRETO)
    rect_text2 = texto_formatado_2.get_rect()
    rect_text3 = texto_formatado_3.get_rect()

    TELA.blit(texto_formatado_2, (LARGURA // 2 - rect_text2.width // 2, ALTURA // 2 - rect_text2.height // 2 - rect_text3.height // 2))
    TELA.blit(texto_formatado_3, (LARGURA // 2 - rect_text3.width // 2, ALTURA // 2 - rect_text3.height // 2 + rect_text3.height // 2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return


def aumenta_vel(pts):
    if pts <= 60 and pts % 5 == 0:
        return 1

    elif pts % 10 == 0:
        return 1
    
    else:
        return 0

#  ----------------- Função main ---------------------------


def main():
    pygame.mixer.music.play(-1)

    #  ---------------- Variáveis alteráveis ----------------------
    x_cobra = ((LARGURA // TAMANHO_COBRA) // 2) * TAMANHO_COBRA
    y_cobra = (2 + (ALTURA // TAMANHO_COBRA) // 2) * TAMANHO_COBRA

    x_maca = TAMANHO_COBRA * randint(0, (LARGURA // TAMANHO_COBRA) - 1)
    y_maca = TAMANHO_COBRA * randint(2, (ALTURA // TAMANHO_COBRA) - 1)

    x_controle = VEL
    y_controle = 0

    pontos = 0

    lista_cobra = []

    if aumentar_velocidade is False:
        fps = 15
    else:
        fps = 8
    pos_maca = []
    #  --------------- Loop principal ------------------------
    while True:
        CLOCK.tick(fps)
        TELA.fill(BRANCO)

        mensagem_1 = f'Pontos: {pontos}'
        texto_formatado_1 = FONTE_PONTOS.render(mensagem_1, True, PRETO)
        rect_text1 = texto_formatado_1.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x_controle != VEL:  # Esquerda
                    x_controle = -VEL
                    y_controle = 0

                elif event.key == pygame.K_d and x_controle != -VEL:  # Direita
                    x_controle = VEL
                    y_controle = 0

                elif event.key == pygame.K_w and y_controle != VEL:  # Cima
                    y_controle = -VEL
                    x_controle = 0

                elif event.key == pygame.K_s and y_controle != -VEL:  # Baixo
                    y_controle = VEL
                    x_controle = 0

        x_cobra += x_controle
        y_cobra += y_controle

        if x_cobra >= LARGURA:
            x_cobra = 0
        if x_cobra < 0:
            x_cobra = LARGURA - TAMANHO_COBRA
        if y_cobra >= ALTURA:
            y_cobra = 40
        if y_cobra < 40:
            y_cobra = ALTURA - TAMANHO_COBRA

        maca = pygame.draw.rect(TELA, VERMELHO, (x_maca, y_maca, TAMANHO_MACA, TAMANHO_MACA))
        cobra = pygame.draw.rect(TELA, VERDE, (x_cobra, y_cobra, TAMANHO_COBRA, TAMANHO_COBRA))

        if cobra.colliderect(maca):
            pontos += 1
            som_maca.play()
            while True:
                x_maca = TAMANHO_COBRA * randint(0, (LARGURA // TAMANHO_COBRA) - 1)
                y_maca = TAMANHO_COBRA * randint(2, (ALTURA // TAMANHO_COBRA) - 1)
                pos_maca = [x_maca, y_maca]
                if lista_cobra.count(pos_maca) == 0:
                    break
            
            if aumentar_velocidade is True and aumenta_vel(pontos) != 0:
                fps += aumenta_vel(pontos)
                som_maca.stop()
                som_speedup.play()

        TELA.blit(texto_formatado_1, (LARGURA - rect_text1.width - 2, 2))  # Mostrando os pontos
        pygame.draw.rect(TELA, PRETO, (0, 39, LARGURA, 2))

        posicao_cabeca = []
        posicao_cabeca.append(x_cobra)
        posicao_cabeca.append(y_cobra)

        lista_cobra.append(posicao_cabeca)

        if len(lista_cobra) > pontos + 3:
            del lista_cobra[0]

        aumenta_cobra(lista_cobra)

        if aumentar_velocidade is True:
            mensagem_4 = f'Velocidade: {fps / 10}x'
            texto_formatado_4 = FONTE_VELOCIDADE.render(mensagem_4, True, PRETO)
            TELA.blit(texto_formatado_4, (2, texto_formatado_4.get_rect().height // 2 + 2))

        if lista_cobra.count(posicao_cabeca) > 1:
            pygame.mixer.music.stop()
            som_gameover.play()
            game_over(pontos)
            main()

        pygame.display.update()


#  --------------------------- Iniciando o jogo -------------------------
if __name__ == '__main__':
    main()

# pyi-makespec.exe --onefile --icon="arquivos/snake-icon.ico" --noconsole .\jogo_cobrinha.py
# pyinstaller.exe .\jogo_cobrinha.spec
