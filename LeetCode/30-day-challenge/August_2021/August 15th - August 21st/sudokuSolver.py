"""
    Problem Link:- https://leetcode.com/problems/sudoku-solver/
"""


def sudoku_solver(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for k in range(1, 10):
                    if is_valid(board, i, j, str(k)):
                        board[i][j] = str(k)

                        if sudoku_solver(board):
                            return True
                        else:
                            board[i][j] = "."

                return False

    return True


def is_valid(board, i, j, k):
    nRow = 3 * (i // 3)
    nCol = 3 * (j // 3)

    for m in range(9):
        if board[i][m] == k:
            return False

        if board[m][j] == k:
            return False

        if board[nRow + m // 3][nCol + m % 3] == k:
            return False

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
sudoku_solver(board)
print(board)
