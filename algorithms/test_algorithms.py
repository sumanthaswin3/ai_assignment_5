from minimax import find_best_move
from game import *


board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    [' ', ' ', ' ']
]

move = find_best_move(board)
print('Test Passed' if move == (2, 1) else 'Test Failed')
