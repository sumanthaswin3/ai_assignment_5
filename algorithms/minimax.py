EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'


def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False


def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == PLAYER_X else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 10 if board[0][col] == PLAYER_X else -10

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == PLAYER_X else -10

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == PLAYER_X else -10

    return 0
