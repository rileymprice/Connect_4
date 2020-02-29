import numpy as np
import sys
import math
import random

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7
MAX_HEIGHT_RULE = 2
GAME_OVER = False
PLAYERS = [1, 2]


def create_board():
    """Creates NP 2d array filled with zeros the size of connect4 board"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, col, piece):
    """Drops piece in the next available row in the given column"""
    row = get_next_open_row(board, col)
    board[row][col] = piece


def is_valid_location(board, col):
    """Checks if there is a valid spot in the given column.
       Rule is we cannot place piece more than 2 pieces above the rest of the board"""
    target_row = get_next_open_row(board, col)
    if target_row > -1:
        if board[target_row][col] == 0:
            if target_row + 1 < MAX_HEIGHT_RULE:
                return True
            else:
                if max(board[target_row - MAX_HEIGHT_RULE]) > 0:
                    return True
                else:
                    return False
        return False
    return False


def get_next_open_row(board, col):
    """Returns the next available row in given column, otherwise returns -1s"""
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row
        else:
            return -1


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    # for c in range(COLUMN_COUNT - 3):
    #     for r in range(ROW_COUNT):
    #         if (
    #             board[r][c] == piece
    #             and board[r][c + 1] == piece
    #             and board[r][c + 2] == piece
    #             and board[r][c + 3] == piece
    #         ):
    #             return True

    # # Check vertical locations for win
    # for c in range(COLUMN_COUNT):
    #     for r in range(ROW_COUNT - 3):
    #         if (
    #             board[r][c] == piece
    #             and board[r + 1][c] == piece
    #             and board[r + 2][c] == piece
    #             and board[r + 3][c] == piece
    #         ):
    #             return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True


board = create_board()

while not GAME_OVER:
    turn = random.randint
