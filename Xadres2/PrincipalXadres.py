"""Esse arquivo vai ser destinado para armazenar todas as informações dentro da execução do jogo e vai determinar os movimentos válidos nas quais as peças fazem, e tambem vai fazer um *log de movimentos"""


import pygame as p 
import EngineXadres


WIDTH = HEIGHT = 512 #múltiplo quadrático
DIMENSION = 8 #um tabuleiro de xadrez é 8x8
SQ_SIZE = WIDTH / DIMENSION #tamanho dos quadrados do tabuleiro, por isso que 512 é melhor 400 na resolução
MAX_FPS = 15 #para possíveis animações futuras
IMAGES = {}

def loadImages():
    pecas = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for peca in pecas:
        IMAGES[peca] = p.transform.scale(p.image.load("images/" + peca + ".png"), (SQ_SIZE, SQ_SIZE))
        
        
"""Aqui vai ser onde o usuario irá fazer os inputs e atualizar o processo de imagem do jogo"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = EngineXadres.GameState()
    #print(gs.tabuleiro)
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                #esse if vai de acordo com as PREPs que o python recomenda, normalmente usado para importar ações como esse "principal" em outra 
        clock.tick(MAX_FPS)
        p.display.flip()
    
#desenhando tabuleiro e peças/responsavel pelas atualizacoes graficas no jogo

def drawGameState(screen, gs):
    drawTabuleiro(screen)
    drawPecas(screen,gs.tabuleiro)
    
#desenha os quadrados no tabuleiro/o quadrado ESQUEDAR SUPERIOR sempre sera CLARO
def drawTabuleiro(screen):
    cores = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            cores[((r+c)%2)]
            p.draw.rect(screen, cores, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            

#desenha as peças no tabuleiro
def drawPecas(screen, tabuleiro):
    pass