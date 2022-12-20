import pygame
import random as r
import settings as s
import numpy as np
import sys
from Botao import botao
from pygame.locals import *
from sys import exit
import msc

pygame.init()

def get_font(size):
    return pygame.font.Font("assets/GillSansUltraBold.ttf", size)

def telaSaldo():

    msc.som_saldoInsuficiente()

    while True:
        s.ImagemBotao = pygame.transform.scale(s.ImagemBotao, (280, 74))
        s.tela.blit(s.ImagemSaldo, (0,0))

        pos_mouse_tela = pygame.mouse.get_pos()

        botao_adicionar = botao(image=s.ImagemBotao, pos=(241, 650), 
                                text_input="ADICIONAR 500 MOEDAS", font=get_font(15), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_adicionar]:
                button.changeColor(pos_mouse_tela)
                button.update(s.tela)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_adicionar.checkForInput(pos_mouse_tela):
                        s.som_click.play()
                        s.carteira = s.carteira + 500
                        telaAposta()

        pygame.display.update()


def telaAviso():

    msc.Aposta()

    while True:
        s.ImagemBotao = pygame.transform.scale(s.ImagemBotao, (250, 74))
        s.tela.blit(s.ImagemAviso, (0,0))

        pos_mouse_tela = pygame.mouse.get_pos()

        botao_voltar2 = botao(image=s.ImagemBotao, pos=(241, 650), 
                                text_input="VOLTAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_voltar2]:
                button.changeColor(pos_mouse_tela)
                button.update(s.tela)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar2.checkForInput(pos_mouse_tela):
                        telaAposta()

        pygame.display.update()


def telaGanhou():

    msc.musica_ganhou()

    font2 = pygame.font.SysFont(None, 40)

    while True:
        s.tela.blit(s.ImagemGanhou, (0,0))

        numeros = font2.render(str(s.numeroSorteado), True, ("#ff0000"))
        numeros2 = font2.render(str(s.numeroAposta), True, ("#ff0000"))

        if s.multiplicador == 18:
            s.tela.blit(numeros, (217, 546))
        else:
            s.tela.blit(numeros, (142, 548))

        if s.numeroAnimal == 0:
            s.tela.blit(numeros2, (156, 629))
        else:
            s.tela.blit(numeros2, (120, 629))

        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(dinheiro, (230, 260))
        s.tela.blit(s.coin, (190,252))

        pos_mouse_tela = pygame.mouse.get_pos()

        s.ImagemBotao = pygame.transform.scale(s.ImagemBotao, (220, 74))
        botao_voltar = botao(image=s.ImagemBotao, pos=(241, 730), 
                            text_input="VOLTAR", font=get_font(25), base_color="#f5f7f5", hovering_color="Green")


        for button in [botao_voltar]:
            button.changeColor(pos_mouse_tela)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_tela):
                    s.numeroAposta = []
                    telaAposta()

        pygame.display.update()

def telaPerdeu():

    msc.musica_perdeu()

    font2 = pygame.font.SysFont(None, 40)

    while True:
        s.tela.blit(s.ImagemPerdeu, (0,0))

        numeros = font2.render(str(s.numeroSorteado), True, ("#ff0000"))
        numeros2 = font2.render(str(s.numeroAposta), True, ("#ff0000"))

        if s.multiplicador == 18:
            s.tela.blit(numeros, (217, 546))
        else:
            s.tela.blit(numeros, (142, 548))

        if s.numeroAnimal == 0:
            s.tela.blit(numeros2, (156, 629))
        else:
            s.tela.blit(numeros2, (120, 629))

        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(dinheiro, (230, 260))
        s.tela.blit(s.coin, (190,252))

        pos_mouse_tela = pygame.mouse.get_pos()

        s.ImagemBotao = pygame.transform.scale(s.ImagemBotao, (220, 74))
        botao_voltar = botao(image=s.ImagemBotao, pos=(241, 730), 
                            text_input="VOLTAR", font=get_font(25), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_tela)
            button.update(s.tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_tela):
                    s.som_click.play()
                    s.numeroAposta = []
                    telaAposta()

        pygame.display.update()

def telaAposta():

    msc.tela_aposta()

    font2 = pygame.font.SysFont(None, 40)

    while True:
        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(s.ImagemEscolha, (0,0))
        s.tela.blit(dinheiro, (390, 145))
        s.tela.blit(s.coin, (350,135))
        
        pos_mouse_jogar = pygame.mouse.get_pos()

        botao_voltar = botao(image=pygame.image.load("assets/botaovoltar.png"), pos=(430, 750), 
                            text_input=".", font=get_font(25), base_color="#ffffff", hovering_color="Red")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_major = botao(image=pygame.image.load("assets/majorporco.png"), pos=(139, 337), 
                            text_input=".", font=get_font(25), base_color="#ffdbbc", hovering_color="Red")

        for button in [botao_major]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)
        
        botao_cavalo = botao(image=pygame.image.load("assets/cavalosansao.png"), pos=(244, 336), 
                            text_input=".", font=get_font(25), base_color="#d0cbc9", hovering_color="Red")

        for button in [botao_cavalo]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_cabra = botao(image=pygame.image.load("assets/cabramaricota.png"), pos=(348, 335), 
                            text_input=".", font=get_font(25), base_color="#d9d9d6", hovering_color="Red")

        for button in [botao_cabra]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_boladeneve = botao(image=pygame.image.load("assets/porcoboladeneve.png"), pos=(138, 439), 
                            text_input=".", font=get_font(25), base_color="#fdd5b7", hovering_color="Red")

        for button in [botao_boladeneve]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_burro = botao(image=pygame.image.load("assets/burro.png"), pos=(239, 446), 
                            text_input=".", font=get_font(25), base_color="#4c0000", hovering_color="Red")

        for button in [botao_burro]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_quiteria = botao(image=pygame.image.load("assets/eguaquiteria.png"), pos=(346, 442), 
                            text_input=".", font=get_font(25), base_color="#906b59", hovering_color="Red")

        for button in [botao_quiteria]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_mimosa = botao(image=pygame.image.load("assets/eguamimosa.png"), pos=(138, 550), 
                            text_input=".", font=get_font(25), base_color="#ac8a72", hovering_color="Red")

        for button in [botao_mimosa]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_corvo = botao(image=pygame.image.load("assets/corvo.png"), pos=(241, 556), 
                            text_input=".", font=get_font(25), base_color="#33314c", hovering_color="Red")

        for button in [botao_corvo]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_ovelhas = botao(image=pygame.image.load("assets/ovelhas.png"), pos=(344, 555), 
                            text_input=".", font=get_font(25), base_color="#49494a", hovering_color="Red")

        for button in [botao_ovelhas]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_cachorro = botao(image=pygame.image.load("assets/cachorro.png"), pos=(141, 669), 
                            text_input=".", font=get_font(25), base_color="#ff7610", hovering_color="Red")

        for button in [botao_cachorro]:
            button.changeColor(pos_mouse_jogar)
            button.update(s.tela)

        botao_napoleao = botao(image=pygame.image.load("assets/porconapoleao.png"), pos=(246, 673), 
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
                if botao_voltar.checkForInput(pos_mouse_jogar):
                    s.som_click.play()
                    s.numeroAposta = []
                    menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_major.checkForInput(pos_mouse_jogar):
                    s.som_major_porco.play()
                    s.numeroAposta = [1,2,3,4,5]
                    s.numeroAnimal = 0
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cavalo.checkForInput(pos_mouse_jogar):
                    s.som_cavalo_sansao.play()
                    s.numeroAposta = [6,7,8,9,10]
                    s.numeroAnimal = 0
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cabra.checkForInput(pos_mouse_jogar):
                    s.som_cabra_maricota.play()
                    s.numeroAposta = [11,12,13,14,15]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_boladeneve.checkForInput(pos_mouse_jogar):
                    s.som_porco_bola_de_neve.play()
                    s.numeroAposta = [16,17,18,19,20]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_burro.checkForInput(pos_mouse_jogar):
                    s.som_burro_benjamin.play()
                    s.numeroAposta = [21,22,23,24,25]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_quiteria.checkForInput(pos_mouse_jogar):
                    s.som_egua_quiteria.play()
                    s.numeroAposta = [26,27,28,29,30]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_mimosa.checkForInput(pos_mouse_jogar):
                    s.som_egua_mimosa.play()
                    s.numeroAposta = [31,32,33,34,35]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_corvo.checkForInput(pos_mouse_jogar):
                    s.som_corvo_moises.play()
                    s.numeroAposta = [36,37,38,39,40]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_ovelhas.checkForInput(pos_mouse_jogar):
                    s.som_ovelhas.play()
                    s.numeroAposta = [41,42,43,44,45]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_cachorro.checkForInput(pos_mouse_jogar):
                    s.som_cachorro_catavento.play()
                    s.numeroAposta = [46,47,48,49,50]
                    s.numeroAnimal = 1
                    botoes_valores()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_napoleao.checkForInput(pos_mouse_jogar):
                    s.som_porco_napoleao.play()
                    s.numeroAposta = [51,52,53,54,55]
                    s.numeroAnimal = 1
                    botoes_valores()

        pygame.display.update()

def botoes_valores():
    font2 = pygame.font.SysFont(None, 40)

    while True:

        s.tela.blit(s.ImagemValor, (0,0))
        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, (255,255,255))
        s.tela.blit(dinheiro, (390, 145))
        s.tela.blit(s.coin, (350,135))
        numeros = font2.render(str(s.numeroAposta), True, ("#ff0000"))
        
        if s.numeroAnimal == 0:
            s.tela.blit(numeros, (155, 242))
        else:
            s.tela.blit(numeros, (120, 242))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_voltar = botao(image=pygame.image.load("assets/botaovoltar.png"), pos=(430, 750), 
                            text_input=".", font=get_font(25), base_color="#ffffff", hovering_color="Red")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        botao_aposta100 = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 410), 
                            text_input="100", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta100]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)
        
        botao_aposta250 = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 535), 
                            text_input="250", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_aposta250]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

        botao_aposta500 = botao(image=pygame.image.load("assets/botao1.png"), pos=(240, 660), 
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
                    s.som_click.play()
                    if s.carteira <= 0 or s.carteira < 100:
                        telaSaldo()
                    else: 
                        s.valorAposta = 100
                        selecaoPremio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta250.checkForInput(pos_mouse_menu):
                    s.som_click.play()
                    if s.carteira <= 0 or s.carteira < 250:
                        telaSaldo()
                    else: 
                        s.valorAposta = 250
                        selecaoPremio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aposta500.checkForInput(pos_mouse_menu):
                    s.som_click.play()
                    if s.carteira <= 0 or s.carteira < 500:
                        telaSaldo()
                    else: 
                        s.valorAposta = 500
                        selecaoPremio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_menu):
                    s.som_click.play()
                    s.numeroAposta = []
                    telaAposta()

        pygame.display.update()

def selecaoPremio():
    font2 = pygame.font.SysFont(None, 40)
    
    while True:
        s.tela.blit(s.ImagemPremio, (0,0))

        s.coin = pygame.transform.scale(s.coin, (40, 40))
        dinheiro = font2.render(str(s.carteira), True, ("#FF4500"))
        s.tela.blit(dinheiro, (230, 235))
        s.tela.blit(s.coin, (190,225))

        pos_mouse_menu = pygame.mouse.get_pos()

        botao_voltar = botao(image=pygame.image.load("assets/botaovoltar.png"), pos=(430, 750), 
                            text_input=".", font=get_font(25), base_color="#ffffff", hovering_color="Red")

        for button in [botao_voltar]:
            button.changeColor(pos_mouse_menu)
            button.update(s.tela)

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
                    s.som_click.play()
                    s.multiplicador = 18
                    apostar()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_primeiroQuintoPremio.checkForInput(pos_mouse_menu):
                    s.som_click.play()
                    s.multiplicador = 3.6
                    apostar()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.checkForInput(pos_mouse_menu):
                    s.som_click.play()
                    s.valorAposta = 0
                    botoes_valores() 

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
                    s.som_click.play()
                    if s.multiplicador == 18:
                        s.numeroSorteado = np.random.randint(1, 56, (1))
                        s.lista_historico.append(s.numeroSorteado)
                        with open('historico_sorteio.txt', "w") as resultados:
                            for item in s.lista_historico:
                                resultados.write("%s\n" % item)  
                            resultados.close()
                        numerosAcertados = set(s.numeroAposta).intersection(s.numeroSorteado)
                        if numerosAcertados:
                            s.carteira =  s.carteira + (s.valorAposta * s.multiplicador)
                            telaGanhou()
                        else:
                            s.carteira = s.carteira - s.valorAposta
                            telaPerdeu()
                    else:
                        s.numeroSorteado = np.random.randint(1, 56, (5))
                        s.lista_historico.append(s.numeroSorteado)
                        with open('historico_sorteio.txt', "w") as resultados:
                            for item in s.lista_historico:
                                resultados.write("%s\n" % item)  
                            resultados.close()
                        numerosAcertados = set(s.numeroAposta).intersection(s.numeroSorteado)
                        if numerosAcertados:
                            s.carteira =  s.carteira + (s.valorAposta * s.multiplicador)
                            telaGanhou()
                        else:
                            s.carteira = s.carteira - s.valorAposta
                            telaPerdeu()
       
        pygame.display.update() 

def menu():

    msc.musica_menu()

    while True:
        
        s.tela.blit(s.ImagemFundo, (0,0))

        pos_mouse_tela = pygame.mouse.get_pos()

        botao_jogar = botao(image=pygame.image.load("assets/botao1.png"), pos=(239, 548), 
                            text_input="JOGAR", font=get_font(30), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_jogar]:
            button.changeColor(pos_mouse_tela)
            button.update(s.tela)

        s.ImagemBotao = pygame.transform.scale(s.ImagemBotao, (220, 74))
        botao_historico = botao(image=s.ImagemBotao, pos=(241, 730), 
                        text_input="Histórico", font=get_font(25), base_color="#f5f7f5", hovering_color="Green")

        for button in [botao_historico]:
            button.changeColor(pos_mouse_tela)
            button.update(s.tela)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.checkForInput(pos_mouse_tela):
                    s.som_click.play()
                    telaAposta()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_historico.checkForInput(pos_mouse_tela):
                    s.som_click.play()
                    historico()

        pygame.display.update()

def historico():
     
    with open('historico_sorteio.txt', "r") as resultados:
        line_numbers = [0, 1, 2, 3]
        lines = []
        for i, line in enumerate(resultados):
            if i in line_numbers:
                lines.append(line.strip())
            elif i > 3:
                break
        lista = ', '.join(lines)

    ativo = True
    while ativo:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                ativo = False
                pygame.quit()   
                sys.exit()         
            if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()
        
        font = pygame.font.Font('assets/GillSansUltraBold.ttf', 15)
        s.tela.blit(s.ImagemHistorico, (0,0))
        texto = font.render ("Últimas Dezenas Sorteadas:", True, 'White')
        s.tela.blit(texto, (120, 370))
        text = font.render ("CLIQUE NA TELA PARA RETORNAR AO MENU", True, 'White')
        s.tela.blit(text, (35, 650))
        img = font.render(lista, True, 'White')
        s.tela.blit(img, (70, 400))
        pygame.display.update()
menu()
