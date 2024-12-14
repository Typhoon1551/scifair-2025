import minimax as mx
import ml
import random

def run_game(ai_agent):
    board = [random.randrange(1,6) for i in range(random.randrange(2,6))]
    player = random.choice(['mx','ml'])

    #print(board)

    while sum(board) != 0:
        #print(player)
        match player:
            case'mx':
                board = mx.decide(board, -float('inf'), float('inf'), True)[1][1]
                player = 'ml'
            case 'ml':
                pile, count = ai_agent.choose_action(board, epsilon=False)
                board[pile] -= count
                player = 'mx'
        #print(board)

    return player

def run_series(games, ai_agent):
    score = [0,0,0]

    for i in range(games):
        match run_game(ai_agent):
            case 'mx':
                score[0] += 1
            case 'ml':
                score[1] += 1
        score[2] += 1

    return score

if __name__ == '__main__':
    increments = [10000, 50000, 100000, 500000, 1000000]

    for i in increments:
        ai = ml.train(i)
        print(f'trained over {i} games')

        r = run_series(1000, ai)
        print(f'final score: {r}')
