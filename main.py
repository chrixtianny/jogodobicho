import pygame
import random as r
import settings as s
import numpy as np
from botao import botao
from pygame.locals import *
from sys import exit

pygame.init()

def get_font(size):
    return pygame.font.Font("assets/GillSansUltraBold.ttf", size)

def telaAviso():
    while True:
        s.ImagemBotao = pygame.transform.scale(s.ImagemBotao, (250, 74))
        s.tela.blit(s.ImagemAviso, (0,0))

        pos_mouse_telaAviso = pygame.mouse.get_pos()

        botao_voltar2 = botao(image=s.ImagemBotao, pos=(241, 650), 
                                text_input="VOLTAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_voltar2]:
                button.changeColor(pos_mouse_telaAviso)
                button.update(s.tela)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar2.checkForInput(pos_mouse_telaAviso):
                        telaAposta()

        pygame.display.update()

def telaGanhou():
    font2 = pygame.font.SysFont(None, 40)

    while True:
        s.tela.blit(s.ImagemGanhou, (0,0))

        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(dinheiro, (380, 50))
        s.tela.blit(s.coin, (340,40))

        pos_mouse_tela = pygame.mouse.get_pos()

        botao_voltar = botao(image=pygame.image.load("assets/botao1.png"), pos=(241, 650), 
                            text_input="VOLTAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_tela)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_tela):
                    print(s.numeroAposta)
                    telaAposta()

        pygame.display.update()

def telaPerdeu():
    font2 = pygame.font.SysFont(None, 40)

    while True:
        s.tela.blit(s.ImagemPerdeu, (0,0))

        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(dinheiro, (390, 50))
        s.tela.blit(s.coin, (350,40))

        pos_mouse_tela = pygame.mouse.get_pos()

        botao_voltar = botao(image=pygame.image.load("assets/botao1.png"), pos=(241, 650), 
                            text_input="VOLTAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_tela)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_tela):
                    print(s.numeroAposta)
                    telaAposta()


        pygame.display.update()

def telaAposta():
    font2 = pygame.font.SysFont(None, 40)

    while True:
        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(s.ImagemEscolha, (0,0))
        s.tela.blit(dinheiro, (390, 50))
        s.tela.blit(s.coin, (350,40))
        
        pos_mouse_jogar = pygame.mouse.get_pos()

        botao_major = botao(image=pygame.image.load("assets/majorporco.png"), pos=(139, 264), 
                            text_input=".", font=get_font(25), base_color="#ffdbbc", hovering_color="Red")

        for button in [botao_major]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)
        
        botao_cavalo = botao(image=pygame.image.load("assets/cavalosansao.png"), pos=(244, 263), 
                            text_input=".", font=get_font(25), base_color="#d0cbc9", hovering_color="Red")

        for button in [botao_cavalo]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_cabra = botao(image=pygame.image.load("assets/cabramaricota.png"), pos=(348, 262), 
                            text_input=".", font=get_font(25), base_color="#d9d9d6", hovering_color="Red")

        for button in [botao_cabra]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_boladeneve = botao(image=pygame.image.load("assets/porcoboladeneve.png"), pos=(138, 366), 
                            text_input=".", font=get_font(25), base_color="#fdd5b7", hovering_color="Red")

        for button in [botao_boladeneve]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_burro = botao(image=pygame.image.load("assets/burro.png"), pos=(239, 373), 
                            text_input=".", font=get_font(25), base_color="#4c0000", hovering_color="Red")

        for button in [botao_burro]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_quiteria = botao(image=pygame.image.load("assets/eguaquiteria.png"), pos=(346, 369), 
                            text_input=".", font=get_font(25), base_color="#906b59", hovering_color="Red")

        for button in [botao_quiteria]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_mimosa = botao(image=pygame.image.load("assets/eguamimosa.png"), pos=(138, 477), 
                            text_input=".", font=get_font(25), base_color="#ac8a72", hovering_color="Red")

        for button in [botao_mimosa]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_corvo = botao(image=pygame.image.load("assets/corvo.png"), pos=(241, 483), 
                            text_input=".", font=get_font(25), base_color="#33314c", hovering_color="Red")

        for button in [botao_corvo]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_ovelhas = botao(image=pygame.image.load("assets/ovelhas.png"), pos=(344, 482), 
                            text_input=".", font=get_font(25), base_color="#49494a", hovering_color="Red")

        for button in [botao_ovelhas]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_cachorro = botao(image=pygame.image.load("assets/cachorro.png"), pos=(141, 596), 
                            text_input=".", font=get_font(25), base_color="#ff7610", hovering_color="Red")

        for button in [botao_cachorro]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_napoleao = botao(image=pygame.image.load("assets/porconapoleao.png"), pos=(246, 600), 
                            text_input=".", font=get_font(25), base_color="#ffd6b7", hovering_color="Red")

        for button in [botao_napoleao]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_valores = botao(image=pygame.image.load("assets/botao2.png"), pos=(240, 738), 
                            text_input="VALORES", font=get_font(25), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_valores]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_major.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [1,2,3,4,5]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cavalo.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [6,7,8,9,10]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cabra.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [11,12,13,14,15]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_boladeneve.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [16,17,18,19,20]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_burro.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [21,22,23,24,25]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_quiteria.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [26,27,28,29,30]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_mimosa.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [31,32,33,34,35]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_corvo.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [36,37,38,39,40]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_ovelhas.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [41,42,43,44,45]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cachorro.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [46,47,48,49,50]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_napoleao.checkForInput(pos_mouse_jogar):
                    s.numeroAposta = [51,52,53,54,55]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_valores.checkForInput(pos_mouse_jogar):
                    if s.numeroAposta == []:
                        telaAviso()
                    else:
                        botoes_apostas()

        pygame.display.update()

def botoes_apostas():
    while True:
        
        s.tela.blit(s.ImagemValor, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_voltar = botao(image=pygame.image.load("assets/botaovoltar.png"), pos=(430, 750), 
                            text_input=".", font=get_font(25), base_color="#ffffff", hovering_color="Red")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        botao_aposta100 = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 400), 
                            text_input="100", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta100]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)
        
        botao_aposta250 = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 525), 
                            text_input="250", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta250]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        botao_aposta500 = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 650), 
                            text_input="500", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta500]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta100.checkForInput(pos_mouse_menu):
                    s.valorAposta = 100
                    selecaoPremio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta250.checkForInput(pos_mouse_menu):
                    s.valorAposta = 250
                    selecaoPremio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta500.checkForInput(pos_mouse_menu):
                    s.valorAposta = 500
                    selecaoPremio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_menu):
                    s.numeroAposta = []
                    telaAposta()

        pygame.display.update()

def selecaoPremio():
    while True:
        s.tela.blit(s.ImagemPremio, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_primeiroPremio = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 475), 
                            text_input="1°", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_primeiroPremio]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        botao_primeiroQuintoPremio = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 600), 
                            text_input="1° ao 5°", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_primeiroQuintoPremio]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_primeiroPremio.checkForInput(pos_mouse_menu):
                    s.multiplicador = 18
                    apostar()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_primeiroQuintoPremio.checkForInput(pos_mouse_menu):
                    s.multiplicador = 3.6
                    apostar()

        pygame.display.update()

def apostar():
    while True:
        s.tela.blit(s.ImagemAposta, (0,0))

        pos_mouse_apostar = pygame.mouse.get_pos()

        botao_apostar = botao(image=pygame.image.load("assets/botao1.png"), pos=(239, 485), 
                            text_input="APOSTAR!", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_apostar]:
            button.changeColor(pos_mouse_apostar)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_apostar.checkForInput(pos_mouse_apostar):
                    s.numeroSorteado = np.random.randint(1, 56, (5))
                    numerosAcertados = set(s.numeroAposta).intersection(s.numeroSorteado)
                    if numerosAcertados:
                        print(s.numeroSorteado)
                        s.carteira =  s.carteira + (s.valorAposta * s.multiplicador)
                        telaGanhou()
                    else:
                        print(s.numeroSorteado)
                        s.carteira = s.carteira - s.valorAposta
                        telaPerdeu()
       
        pygame.display.update() 

def menu():
    while True:
        
        s.tela.blit(s.ImagemFundo, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_jogar = botao(image=pygame.image.load("assets/botao1.png"), pos=(239, 548), 
                            text_input="JOGAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_jogar]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.checkForInput(pos_mouse_menu):
                    telaAposta()

        pygame.display.update()

menu()