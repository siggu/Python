import numpy as np
def solution(board):
    board = np.array(board)
    for a, b in zip(*np.where(board == 1)):
        board[a-1 if a else 0:a+2, b-1 if b else 0:b+2] = 1
    return len(board[board == 0])