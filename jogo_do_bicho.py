import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 480
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Bicho")
ImagemFundo = pygame.image.load('imagens/fundojogo.png')

class Botao(pygame.sprite.Sprite):
    def __init__(self, *groups):

        super().__init__(*groups)

        self.image = pygame.image.load("imagens/botao1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [270, 84])
        self.rect = pygame.Rect(190, 49, 190, 49)
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load("imagens/botao1.png").convert_alpha()
        self.image2 = pygame.image.load("imagens/botao2.png").convert_alpha()

        self.touche = True

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2
            else:
                self.touche = False
                self.image = self.image1

        pass

ButtonGrups = pygame.sprite.Group()
Botton_1 = Botao(ButtonGrups)
Botton_1.rect.center = (239, 548)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(ImagemFundo, (0,0))
    ButtonGrups.update()
    ButtonGrups.draw(tela)
    pygame.display.update()