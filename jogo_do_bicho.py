import pygame
from Botao import Button
from pygame.locals import *
from sys import exit

pygame.init()

largura = 480
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
ImagemFundo = pygame.image.load("imagens/fundojogo.png")
ImagemFundo2 = pygame.image.load("imagens/fundojogodobicho.png")

def get_font(size):
    return pygame.font.Font("imagens/GillSansUltraBold.ttf", size)

def telaAposta():
    while True:
        tela.blit(ImagemFundo2, (0,0))
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

        botao_jogar = Button(image=pygame.image.load("imagens/botao1.png"), pos=(239, 548), 
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