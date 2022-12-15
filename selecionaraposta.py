import pygame
from Botao import Button
from pygame.locals import *
from sys import exit

pygame.init()

largura = 360
altura = 620

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
#ImagemFundo = pygame.image.load("imagens/fundojogo.png")
ImagemFundo2 = pygame.image.load("fundojogodobicho.png")
valorApostado = 0
valorSorteio = 0
def get_font(size):
    return pygame.font.Font("GillSansUltraBold.ttf", size)

def telaAposta():
    while True:
        tela.blit(ImagemFundo2, (0,0))
        pos_mouse_jogar = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        pygame.display.update()
 

def botoes_apostas():
    while True:
        
        tela.blit(ImagemFundo2, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_aposta100 = Button(image=pygame.image.load("botao1.png"), pos=(180, 300), 
                            text_input="100", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta100]:
            button.changeColor(pos_mouse_menu)
            button.update(tela)
        
        botao_aposta250 = Button(image=pygame.image.load("botao1.png"), pos=(180, 400), 
                            text_input="250", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta250]:
            button.changeColor(pos_mouse_menu)
            button.update(tela)

        botao_aposta500 = Button(image=pygame.image.load("botao1.png"), pos=(180, 500), 
                            text_input="500", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta500]:
            button.changeColor(pos_mouse_menu)
            button.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta100.checkForInput(pos_mouse_menu):
                    valorApostado = 100
                selecaoPremio()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta250.checkForInput(pos_mouse_menu):
                    valorApostado = 250
                selecaoPremio()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta500.checkForInput(pos_mouse_menu):
                    valorApostado = 500
                selecaoPremio()

        pygame.display.update()

def selecaoPremio():
    while True:
        tela.blit(ImagemFundo2, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_primeiroPremio = Button(image=pygame.image.load("botao1.png"), pos=(180, 300), 
                            text_input="1°", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_primeiroPremio]:
            button.changeColor(pos_mouse_menu)
            button.update(tela)

        botao_primeiroQuintoPremio = Button(image=pygame.image.load("botao1.png"), pos=(180, 400), 
                            text_input="1° a 5°", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_primeiroQuintoPremio]:
            button.changeColor(pos_mouse_menu)
            button.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_primeiroPremio.checkForInput(pos_mouse_menu):
                    valorSorteio = (valorApostado * 18)
                tela2()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_primeiroQuintoPremio.checkForInput(pos_mouse_menu):
                    valorSorteio = (valorApostado * 3.6)
                tela2()

        pygame.display.update()

def tela2():
    font = pygame.font.Font('GillSansUltraBold.ttf', 32)
    text = font.render('funcionou', True, "Green", "Blue")
    textRect = text.get_rect()
    textRect.center = (largura // 2, altura // 2)
    while True:
        tela.blit(ImagemFundo2, (0,0))
        tela.blit(text, textRect)
        pos_mouse_jogar = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
       

        pygame.display.update() 

botoes_apostas()