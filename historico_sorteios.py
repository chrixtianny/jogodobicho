import pygame
import sys

pygame.init()
largura = 360
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
ImagemFundo2 = pygame.image.load("fundo_historico.png")

ultimos_sorteios = open('historico_sorteio.txt', "r")
font = pygame.font.Font('GillSansUltraBold.ttf', 35)

pygame.display.update()
for line in ultimos_sorteios:
    text = line

ativo = True
while ativo:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            ativo = False
        tela.blit(ImagemFundo2, (0,0))

        img = font.render(line, True, 'White')
        tela.blit(img, (80, 300))

        pygame.display.update()

ultimos_sorteios.close()

pygame.quit()
sys.exit()