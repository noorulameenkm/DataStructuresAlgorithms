"""
    Problem Link:- https://leetcode.com/problems/valid-sudoku/
"""


def is_valid_sudoku(board):

    hash_set = set()
    for i in range(9):
        for j in range(9):
            number = board[i][j]
            if number != ".":
                row_wise_key = f'{number}_R_{i}'
                col_wise_key = f'{number}_C_{j}'
                box_wise_key = f'{number}_B_{i // 3}_{j // 3}'

                if row_wise_key in hash_set or \
                   col_wise_key in hash_set or \
                   box_wise_key in hash_set:
                    return False

                hash_set.add(row_wise_key)
                hash_set.add(col_wise_key)
                hash_set.add(box_wise_key)

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

print(is_valid_sudoku(board))

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(is_valid_sudoku(board))
