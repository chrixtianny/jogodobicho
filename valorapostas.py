import pygame
from pygame.locals import *
import time
from pygame.locals import *
from sys import exit

pygame.init()

largura = 360
altura = 580
preta = (0,0,0)
branca = (255,255,255)
clock = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
ImagemFundo = pygame.image.load("fundojogodobicho.png")
text = 'valor da aposta'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, preta)

def telaAposta():

    while True:
        tela.blit(ImagemFundo, (0,0))
        pos_mouse_jogar = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        pygame.display.update()

rect = img.get_rect()
rect.topleft = (65, 280)
cursor = Rect(rect.topright, (5, rect.height))

running = True
background = (ImagemFundo)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, branca)
            rect.size=img.get_size()
            cursor.topleft = rect.topright
    
    tela.blit(ImagemFundo, (0,0))
    tela.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(tela, preta, cursor)
    pygame.display.update()

pygame.quit()
