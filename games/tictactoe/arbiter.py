import minimax
import numpy as np
import AI_agent as ai
import random
import time

def convert_board_minimax(board):
    b = []
    for i in range(9):
        match board.state[i]:
            case ' ':
                b.append(0)
            case 'X':
                b.append(+1)
            case 'O':
                b.append(-1)
    return [
        [b[0], b[1], b[2]],
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]],
    ]

def run_game(agent):
    game = ai.TicTacToeGame()
    player = 1 #random.choice([0, 1])
    side_x = player
    while game.playable():
        print(player)
        if player == 0:
            move = agent.play_select_move(game)
        elif player == 1:
            move = minimax_choose(game)
        if move in game.allowed_moves():
            game.make_move(move)
            player = 1 - player
        game.print_board()
        time.sleep(0.5)

def minimax_choose(game):
    print(len(game.allowed_moves()))
    depth = len(game.allowed_moves())
    print(convert_board_minimax(game))
    match game.player:
        case 'X':
            p = -1
        case 'O':
            p = +1
    m = minimax.minimax(convert_board_minimax(game), depth, p)
    print(m)
    n = 6 - (m[1] * 3) + m[0]
    print(n)
    r = list(game.state)
    r[n] = game.player
    print(''.join(r))
    return ''.join(r)

if __name__ == '__main__':
    agent = ai.Agent(ai.TicTacToeGame)
    agent.learn_game(50000)

    run_game(agent)

