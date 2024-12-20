import numpy as np
import minimax.game as game
from minimax.player import PlayerMM, PlayerAB, Player
from minimax.board import Board

#classes

#functions

#main
if __name__ == '__main__':
    g = game.Game(Board(), PlayerAB(10, True), PlayerAB(10, False))
    g.simulateLocalGame()
