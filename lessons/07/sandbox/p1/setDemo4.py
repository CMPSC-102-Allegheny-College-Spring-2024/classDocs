#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 4: Sudoku Solver using Sets")

def is_valid_sudoku(board):
    # Check rows and columns
    for i in range(9):
        if len(set(board[i])) != 9 or len(set(board[j][i] for j in range(9))) != 9:
            return False

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(set(board[x][y] for x in range(i, i+3) for y in range(j, j+3))) != 9:
                return False

    return True

# Example Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(f"Is the Sudoku board valid? {is_valid_sudoku(sudoku_board)}")
