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
VEL = 8
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
    global VEL
    # Jogador
    jogador_largura = 12
    jogador_altura = 80
    p1_x = 40
    p2_x = LARGURA - p1_x - jogador_largura
    p1_y = p2_y = ALTURA // 2 - jogador_altura // 2
    pontos_p1 = pontos_p2 = 0

    # Bolinha
    tam_bolinha = 12
    bolinha_x = LARGURA // 2 - tam_bolinha // 2
    bolinha_y = ALTURA // 2 - tam_bolinha // 2
    bolinha_vel_x = vel_x_init = (randint(300, 600) / 100) * choice([-1, 1])  # Velocidade de 3 a 6
    bolinha_vel_y = vel_y_init = (randint(100, 500) / 100) * choice([-1, 1])  # Velocidade de 1 a 5

    vencedor = 0
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
        
        # Movimento jogadores
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and p1_y >= abs(VEL) - jogador_altura:
            p1_y -= VEL
        if keys_pressed[pygame.K_s] and p1_y <= ALTURA - abs(VEL):
            p1_y += VEL
        if keys_pressed[pygame.K_UP] and p2_y >= abs(VEL) - jogador_altura:
            p2_y -= VEL
        if keys_pressed[pygame.K_DOWN] and p2_y <= ALTURA - abs(VEL):
            p2_y += VEL

        if keys_pressed[pygame.K_SPACE]:  # PROVISÓRIO - Para resetar o jogo. Ver se pode deixar
            main()
        
        p1 = pygame.draw.rect(tela, white, (p1_x, p1_y, jogador_largura, jogador_altura))
        p2 = pygame.draw.rect(tela, white, (p2_x, p2_y, jogador_largura, jogador_altura))

        pygame.draw.rect(tela, white, bolinha)

        # Colisão bolinha com jogadores
        
        if p1.colliderect(bolinha) and bolinha_vel_x < 0:
            bolinha_vel_x *= -1
            bolinha_vel_x += 1
            if bolinha_vel_y < 0:
                bolinha_vel_y -= 1
            else:
                bolinha_vel_y += 1
            paddle_sound.play()

        elif p2.colliderect(bolinha) and bolinha_vel_x > 0:
            bolinha_vel_x *= -1
            bolinha_vel_x -= 1
            if bolinha_vel_y < 0:
                bolinha_vel_y -= 1
            else:
                bolinha_vel_y += 1
            paddle_sound.play()

        # Colisão bolinha com tela
        elif bolinha.y <= 0 or bolinha.y >= ALTURA - tam_bolinha:
            bolinha_vel_y *= -1
            wall_sound.play()
        
        # Movimentando bolinha
        bolinha.x += bolinha_vel_x
        bolinha.y += bolinha_vel_y

        marcou = False
        # Contabilizando pontos
        if bolinha.x < 0:
            pontos_p2 += 1
            marcou = True
            score_sound.play()
        elif bolinha.x + tam_bolinha > LARGURA:
            score_sound.play()
            pontos_p1 += 1
            marcou = True
        
        if marcou:
            bolinha.x = LARGURA // 2 - tam_bolinha // 2
            bolinha_vel_x = vel_x_init
            bolinha_vel_y = vel_y_init

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
