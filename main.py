import pygame
import random as r
import settings as s
from botao import botao
from pygame.locals import *
from sys import exit

pygame.init()

def get_font(size):
    return pygame.font.Font("assets/GillSansUltraBold.ttf", size)

def telaGanhou():
    while True:
        s.tela.blit(s.ImagemGanhou, (0,0))

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
                    telaAposta()

        pygame.display.update()

def telaPerdeu():
    while True:
        s.tela.blit(s.ImagemPerdeu, (0,0))
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

        botao_aposta = botao(image=pygame.image.load("assets/botao2.png"), pos=(240, 738), 
                            text_input="VALOR", font=get_font(25), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_major.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [1,2,3,4,5]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cavalo.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [6,7,8,9,10]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cabra.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [11,12,13,14,15]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_boladeneve.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [16,17,18,19,20]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_burro.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [21,22,23,24,25]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_quiteria.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [26,27,28,29,30]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_mimosa.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [31,32,33,34,35]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_corvo.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [36,37,38,39,40]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_ovelhas.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [41,42,43,44,45]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cachorro.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [46,47,48,49,50]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_napoleao.checkForInput(pos_mouse_jogar):
                    s.valorAposta = [51,52,53,54,55]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta.checkForInput(pos_mouse_jogar):
                    botoes_apostas()
                    
                    '''
                    valores = [1, 2, 3, 4, 5]
                    s.aposta = r.choice(valores)
                    if s.valorAposta == s.aposta:
                        s.carteira = s.carteira + 100
                        telaGanhou()
                    else:
                        s.carteira = s.carteira - 50
                        telaPerdeu()
                    '''

        pygame.display.update()

def botoes_apostas():
    while True:
        
        s.tela.blit(s.ImagemFundo2, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        Button_aposta100 = botao(image=pygame.image.load("assets/botao1.png"), pos=(180, 300), 
                            text_input="100", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [Button_aposta100]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)
        
        Button_aposta250 = botao(image=pygame.image.load("assets/botao1.png"), pos=(180, 400), 
                            text_input="250", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [Button_aposta250]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        Button_aposta500 = botao(image=pygame.image.load("assets/botao1.png"), pos=(180, 500), 
                            text_input="500", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [Button_aposta500]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_aposta100.checkForInput(pos_mouse_menu):
                    valorApostado = 100
                selecaoPremio()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_aposta250.checkForInput(pos_mouse_menu):
                    valorApostado = 250
                selecaoPremio()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_aposta500.checkForInput(pos_mouse_menu):
                    valorApostado = 500
                selecaoPremio()

        pygame.display.update()

def selecaoPremio():
    while True:
        s.tela.blit(s.ImagemFundo2, (0,0))

        pos_mouse_menu = pygame.mouse.get_pos()

        Button_primeiroPremio = botao(image=pygame.image.load("assets/botao1.png"), pos=(180, 300), 
                            text_input="1°", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [Button_primeiroPremio]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        Button_primeiroQuintoPremio = botao(image=pygame.image.load("assets/botao1.png"), pos=(180, 400), 
                            text_input="1° a 5°", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [Button_primeiroQuintoPremio]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_primeiroPremio.checkForInput(pos_mouse_menu):
                    valorSorteio = (s.valorAposta * s.multiplicador_premio1)
                tela2()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button_primeiroQuintoPremio.checkForInput(pos_mouse_menu):
                    valorSorteio = (s.valorAposta * s.multiplicador_premio15)
                tela2()

        pygame.display.update()

def tela2():
    font = pygame.font.Font('assets/GillSansUltraBold.ttf', 32)
    text = font.render('funcionou', True, "Green", "Blue")
    textRect = text.get_rect()
    textRect.center = (s.largura // 2, s.altura // 2)
    while True:
        s.tela.blit(s.ImagemFundo2, (0,0))
        s.tela.blit(text, textRect)
        pos_mouse_jogar = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
       

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