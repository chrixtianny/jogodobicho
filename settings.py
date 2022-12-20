import pygame
import os

lista_historico = []
numeroAnimal = 0
numeroAposta = []
valorAposta = 0
aposta = 0
largura = 480
altura = 800
carteira = 0
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

pygame.mixer.init()

diretorio = os.path.dirname(__file__)
diretorio_songs = os.path.join(diretorio, "songs")

som_click = pygame.mixer.Sound(os.path.join(diretorio_songs, "Click.wav"))
som_click.set_volume(1)

som_major_porco = pygame.mixer.Sound(os.path.join(diretorio_songs, 'major_porco_som.wav'))
som_major_porco.set_volume(0.6)

som_cavalo_sansao = pygame.mixer.Sound(os.path.join(diretorio_songs, 'CavaloSansao.wav'))
som_cavalo_sansao.set_volume(0.6)

som_cabra_maricota = pygame.mixer.Sound(os.path.join(diretorio_songs, 'Cabra_maricota_.wav'))
som_cabra_maricota.set_volume(0.6)

som_porco_bola_de_neve = pygame.mixer.Sound(os.path.join(diretorio_songs, 'porco_napoleao_som.wav'))
som_porco_bola_de_neve.set_volume(0.6)

som_burro_benjamin = pygame.mixer.Sound(os.path.join(diretorio_songs, 'burro_benjamin_.wav'))
som_burro_benjamin.set_volume(0.6)

som_egua_quiteria = pygame.mixer.Sound(os.path.join(diretorio_songs, 'Égua_Quiteria.wav'))
som_egua_quiteria.set_volume(0.6)

som_egua_mimosa = pygame.mixer.Sound(os.path.join(diretorio_songs, 'Egua_mimosa.wav'))
som_egua_mimosa.set_volume(0.6)

som_corvo_moises = pygame.mixer.Sound(os.path.join(diretorio_songs, 'Corvo_moises_.wav'))
som_corvo_moises.set_volume(0.6)

som_ovelhas = pygame.mixer.Sound(os.path.join(diretorio_songs, 'ovelhas_.wav'))
som_ovelhas.set_volume(0.6)

som_cachorro_catavento = pygame.mixer.Sound(os.path.join(diretorio_songs, 'cachorro_catavento_.wav'))
som_cachorro_catavento.set_volume(0.6)

som_porco_napoleao = pygame.mixer.Sound(os.path.join(diretorio_songs, 'porco_napoleao_som.wav'))
som_porco_napoleao.set_volume(0.6)
