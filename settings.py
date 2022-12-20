import pygame

lista_historico = []
numeroAnimal = 0
numeroAposta = []
valorAposta = 0
aposta = 0
largura = 480
altura = 800
carteira = 100
multiplicador = 0
numeroSorteado = []
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
pygame_icon = pygame.image.load("assets/logojogodobicho.png").convert_alpha()
pygame.display.set_icon(pygame_icon)

pos_mouse_tela = pygame.mouse.get_pos()

ImagemBotao = pygame.image.load("assets/botao1.png")
coin = pygame.image.load('assets/Coin.png')
ImagemFundo = pygame.image.load("assets/fundojogo.png")
ImagemFundo2 = pygame.image.load("assets/fundojogodobicho.png")
ImagemGanhou = pygame.image.load("assets/fundoganhou.png")
ImagemPerdeu = pygame.image.load("assets/fundoperdeu.png")
ImagemEscolha = pygame.image.load("assets/fundoescolhabicho.png")
ImagemValor = pygame.image.load("assets/fundoescolhavalor.png")
ImagemPremio = pygame.image.load("assets/fundoescolhapremio.png")
ImagemAposta = pygame.image.load("assets/fundoapostar.png")
ImagemAviso = pygame.image.load("assets/fundoaviso.png")
ImagemSaldo = pygame.image.load("assets/fundosaldoinsuficiente.png")
ImagemHistorico = pygame.image.load("assets/fundo_historico.png")