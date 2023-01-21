import pygame
from pygame.locals import *
from sys import exit
from colors import white, black
from random import randint, choice
import os

root = os.path.dirname(__file__)  

# Constantes do jogo
LARGURA = 980
ALTURA = 640
FPS = 60
VEL_JOG = 10
TAM_LINHA = 8

# Iniciando Pygame
pygame.init()
pygame.mixer.init()

paddle_sound = pygame.mixer.Sound(os.path.join(root, 'audio/pong-paddle.wav'))
score_sound = pygame.mixer.Sound(os.path.join(root, 'audio/pong-score.wav'))
wall_sound = pygame.mixer.Sound(os.path.join(root, 'audio/pong-wall.wav'))
icon = pygame.image.load(os.path.join(root, 'img/pong-icon.png'))

FONTE = pygame.font.SysFont('consolas', 60, False, False)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Pong')
pygame.display.set_icon(icon)

# Funções
def desenha_campo():
    linha_x = LARGURA // 2 - TAM_LINHA // 2
    linha_y = TAM_LINHA
    while linha_y < ALTURA - TAM_LINHA:
        pygame.draw.rect(tela, white, (linha_x, linha_y, TAM_LINHA, TAM_LINHA))
        linha_y += TAM_LINHA * 2


def desenha_jogador(jog_x, jog_y):
    jog = []
    for i in range(9):
        jog.append(pygame.Rect(jog_x, jog_y + (jogador_altura // 9 * i), jogador_largura, jogador_altura // 9))
        # print(p1)
        pygame.draw.rect(tela, white, jog[i])
    return jog


def desenha_pontuacao(pontos_p1, pontos_p2):
    for i in range(2):
        if i == 0:
            texto_formatado = FONTE.render(pontos_p1, True, white)
            rect_texto = texto_formatado.get_rect()
            tela.blit(texto_formatado, (LARGURA // 2 - 40 // 2 - rect_texto.width - 60, 40))
        else:
            texto_formatado = FONTE.render(pontos_p2, True, white)
            rect_texto = texto_formatado.get_rect()
            tela.blit(texto_formatado, (LARGURA // 2 + 40 // 2 + 60, 40))


def game_over(vencedor):
    tela.fill(black)

    texto_formatado = FONTE.render(f'{vencedor} wins!', True, white)
    rect_texto1 = texto_formatado.get_rect()
    tela.blit(texto_formatado, (LARGURA // 2 - rect_texto1.width // 2, 40))
    
    fonte2 = pygame.font.SysFont('consolas', 40, False, False)
    texto_formatado = fonte2.render('Press SPACEBAR to play again', True, white)
    rect_texto2 = texto_formatado.get_rect()
    tela.blit(texto_formatado, (LARGURA // 2 - rect_texto2.width // 2, 40 + rect_texto1.height + 15))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return


def main():
    global VEL_JOG, jogador_altura, jogador_largura
    # Jogador
    jogador_largura = 12
    jogador_altura = 9 * 10
    p1_x = 40
    p2_x = LARGURA - p1_x - jogador_largura
    p1_y = p2_y = ALTURA // 2 - jogador_altura // 2
    pontos_p1 = pontos_p2 = 0
    vencedor = 0

    p1 = pygame.Rect(p1_x, p1_y, jogador_largura, jogador_altura)
    p2 = pygame.Rect(p2_x, p2_y, jogador_largura, jogador_altura)

    # Bolinha
    tam_bolinha = 10
    bolinha_x = LARGURA // 2 - tam_bolinha // 2
    bolinha_y = ALTURA // 2 - tam_bolinha // 2
    bolinha_vel = bolinha_vel_init = 8
    inclinacao_maxima = 3  # Deve ser menor do que a velocidade da bolinha

    vel_x_init = bolinha_vel_x = randint(inclinacao_maxima, bolinha_vel)  * choice([-1, 1])
    vel_y_init = bolinha_vel_y = (bolinha_vel - abs(bolinha_vel_x))  * choice([-1, 1])
    
    bolinha = pygame.Rect(bolinha_x, bolinha_y, tam_bolinha, tam_bolinha)

    clock = pygame.time.Clock()
    while True:  # Loop principal
        clock.tick(FPS)
        tela.fill(black)

        desenha_campo()
        desenha_pontuacao(str(pontos_p1), str(pontos_p2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # if event.type == pygame.KEYDOWN: # Assim não funciona apertar e segurar
            #     if event.key == pygame.K_w:
            #         print('W')
    
        # Desenhando objetos
        p1 = desenha_jogador(p1_x, p1_y)
        p2 = desenha_jogador(p2_x, p2_y)
        pygame.draw.rect(tela, white, bolinha)
        
        # Movimento jogadores
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and p1_y >= abs(VEL_JOG) - jogador_altura:
            p1_y -= VEL_JOG
        if keys_pressed[pygame.K_s] and p1_y <= ALTURA - abs(VEL_JOG):
            p1_y += VEL_JOG
        if keys_pressed[pygame.K_UP] and p2_y >= abs(VEL_JOG) - jogador_altura:
            p2_y -= VEL_JOG
        if keys_pressed[pygame.K_DOWN] and p2_y <= ALTURA - abs(VEL_JOG):
            p2_y += VEL_JOG

        # if keys_pressed[pygame.K_SPACE]:  # Para resetar o jogo
        #     main()
        
        # Colisão bolinha com jogadores
        if bolinha_vel_x < 0:  # p1
            for i in range(9):  # 0 1 2 3 4 5 6 7 8
                if p1[i].colliderect(bolinha):
                    bolinha_vel += 1
                    bolinha_vel_y = ((i-4) * bolinha_vel) / 5  # Se bolinha_vel = 5, então y = -4 -3 -2 -1 0 1 2 3 4
                    if inclinacao_maxima < bolinha_vel:
                        bolinha_vel_y = bolinha_vel_y * inclinacao_maxima / 4
                    bolinha_vel_x = bolinha_vel - abs(bolinha_vel_y) 
                    paddle_sound.play()
                    break

        elif bolinha_vel_x > 0:  # p2
            for i in range(9):  # 0 1 2 3 4 5 6 7 8
                if p2[i].colliderect(bolinha):
                    bolinha_vel += 1
                    bolinha_vel_y = ((i-4) * bolinha_vel) / 5 
                    if inclinacao_maxima < bolinha_vel:
                        bolinha_vel_y = bolinha_vel_y * inclinacao_maxima / 4
                    bolinha_vel_x = -(bolinha_vel - abs(bolinha_vel_y)) 
                    paddle_sound.play()
                    break

        # Colisão bolinha com tela
        if bolinha.y <= 0 or bolinha.y >= ALTURA - tam_bolinha:
            bolinha_vel_y *= -1
            wall_sound.play()
        
        # Movimentando bolinha
        bolinha.x += bolinha_vel_x
        bolinha.y += bolinha_vel_y

        # Contabilizando pontos
        marcou = False
        if bolinha.x < 0:
            pontos_p2 += 1
            marcou = True
            score_sound.play()
        elif bolinha.x + tam_bolinha > LARGURA:
            pontos_p1 += 1
            marcou = True
            score_sound.play()
        
        if marcou:
            bolinha.x = LARGURA // 2 - tam_bolinha // 2
            bolinha_vel_x = vel_x_init
            bolinha_vel_y = vel_y_init
            bolinha_vel = bolinha_vel_init

        # Game over
        if pontos_p1 == 10:
            vencedor = '1'
        elif pontos_p2 == 10:
            vencedor = '2'

        if vencedor:
            game_over(vencedor=f'Player {vencedor}')
            main()

        pygame.display.update()

if __name__ == "__main__":
    main()

# pyi-makespec.exe --onefile --icon="img/pong-icon.ico" --noconsole .\pong.py
# pyinstaller.exe .\pong.spec
