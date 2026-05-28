from game import *


def alpha_beta(board, depth, alpha, beta, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X

                    best = max(best, alpha_beta(board, depth + 1, alpha, beta, False))

                    board[i][j] = EMPTY
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O

                    best = min(best, alpha_beta(board, depth + 1, alpha, beta, True))

                    board[i][j] = EMPTY
                    beta = min(beta, best)

                    if beta <= alpha:
                        break

        return best


if __name__ == '__main__':
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        [' ', ' ', ' ']
    ]

    result = alpha_beta(board, 0, -1000, 1000, True)
    print('Optimal Value:', result)
