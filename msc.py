import pygame
import os
from random import randint
from random import randrange
import settings as s

pygame.mixer.init()

def musica_menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(s.diretorio_songs, "mainMenu.mp3"))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def musica_perdeu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(s.diretorio_songs, 'musicaTriste.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def musica_ganhou():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(s.diretorio_songs, 'A-cloud-morning_.wav'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def som_saldoInsuficiente():
    som_saldoInsuficiente = pygame.mixer.music.load(os.path.join(s.diretorio_songs, 'semSaldo.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)


def tela_aposta():
    Aposta = pygame.mixer.music.load(os.path.join(s.diretorio_songs, 'musicaAposta.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)