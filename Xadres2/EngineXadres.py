"""Esse arquivo vai ser responsável pelos inputs do usuário dentro do jogo e exibir o status atuário do jogo no display
"""
class GameState():
    def __init__ (self):
        self.tabuleiro = [
            ["bR", "bN", "bP", "bK", "bQ", "bP", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wP", "wK", "wQ", "wP", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []
        