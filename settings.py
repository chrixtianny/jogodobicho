import pygame

valorAposta = 0
aposta = 0
largura = 480
altura = 800
carteira = 500
multiplicador_premio1 = 18
multiplicador_premio15 = 3.6
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
pygame_icon = pygame.image.load("assets/logojogodobicho.png").convert_alpha()
pygame.display.set_icon(pygame_icon)

coin = pygame.image.load('assets/Coin.png')
ImagemFundo = pygame.image.load("assets/fundojogo.png")
ImagemFundo2 = pygame.image.load("assets/fundojogodobicho.png")
ImagemGanhou = pygame.image.load("assets/fundoganhou.png")
ImagemPerdeu = pygame.image.load("assets/fundoperdeu.png")
ImagemEscolha = pygame.image.load("assets/fundoescolhabicho.png")