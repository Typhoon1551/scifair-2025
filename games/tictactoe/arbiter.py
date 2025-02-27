import minimax
import numpy as np
import AI_agent as ai
import random
import time

def convert_board_minimax(board, side):
    b = []
    for i in board.state:
        if i == ' ':
            b.append(0)
        elif i == side:
            b.append(+1)
        else:
            b.append(-1)
    return [
        [b[0], b[1], b[2]],
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]],
    ]

def run_game(agent):
    game = ai.TicTacToeGame()
    player = random.choice([0, 1])
    side_x = player
    while game.playable():
        if player == 0:
            move = agent.play_select_move(game)
        elif player == 1:
            move = minimax_choose(game)
        if move in game.allowed_moves():
            game.make_move(move)
            player = 1 - player
    match game.predict_winner(game.state):
        case 'X':
            return side_x
        case 'O':
            return 1 - side_x
        case None:
            return 2

def minimax_choose(game):
    depth = len(game.allowed_moves())
    if depth == 9:
        n = random.randrange(9)
    else:
        match game.player:
            case 'X':
                p = -1
            case 'O':
                p = +1
        m = minimax.minimax(convert_board_minimax(game, game.player), depth, p)
        n = (m[0] * 3) + m[1]
    r = list(game.state)
    r[n] = game.player
    return ''.join(r)

def run_series(num_games, agent):
    results = [0, 0, 0, 0]
    for i in range(num_games):
        r = run_game(agent)
        results[r] += 1
        results[3] += 1
    return results

if __name__ == '__main__':
    agent = ai.Agent(ai.TicTacToeGame)
    e = [10000, 50000, 100000, 500000, 1000000]
    v = [0]

    for i in e:
        agent.learn_game(i - sum(v))
        print(f"agent trained over {i} episodes")

        r = run_series(1000, agent)
        print(r)

        v.append(i)

