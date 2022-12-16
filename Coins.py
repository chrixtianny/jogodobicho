import pygame
from botao import botao
from pygame.locals import *
from sys import exit

pygame.init()

largura = 480
altura = 800
carteira = 200
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
pygame_icon = pygame.image.load("assets/logojogodobicho.png").convert_alpha()
pygame.display.set_icon(pygame_icon)

ImagemFundo = pygame.image.load("assets/fundojogo.png")
ImagemFundo2 = pygame.image.load("assets/fundojogodobicho.png")

def get_font(size):
    return pygame.font.Font("assets/GillSansUltraBold.ttf", size)

def telaAposta():
    global carteira
    font2 = pygame.font.SysFont(None, 40)

    while True:
        coin = pygame.image.load('assets/Coin.png')
        coin = pygame.transform.scale(coin, (40, 40))
        dinheiro = font2.render(str(carteira), True, (255,255,255))
        tela.blit(ImagemFundo2, (0,0))
        tela.blit(dinheiro, (360, 50))
        tela.blit(coin, (320,40))
        pos_mouse_jogar = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

def menu():
    while True:
        
        tela.blit(ImagemFundo, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_jogar = botao(image=pygame.image.load("assets/botao1.png"), pos=(239, 548), 
                            text_input="JOGAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_jogar]:
            button.changeColor(pos_mouse_menu)
            button.update(tela)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.checkForInput(pos_mouse_menu):
                    telaAposta()

        pygame.display.update()

menu()
