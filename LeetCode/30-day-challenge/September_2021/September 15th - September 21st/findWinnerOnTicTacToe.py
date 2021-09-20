from typing import List


"""
    Problem Link:- https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
"""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def find_winner(board):

            # column wise
            for j in range(3):

                count_a, count_b = 0, 0
                for i in range(3):
                    if board[i][j] == 'X':
                        count_a += 1

                    if board[i][j] == 'O':
                        count_b += 1

                if count_a == 3:
                    return "A"

                if count_b == 3:
                    return "B"

            # row wise
            for i in range(3):

                count_a, count_b = 0, 0
                for j in range(3):
                    if board[i][j] == 'X':
                        count_a += 1

                    if board[i][j] == 'O':
                        count_b += 1

                if count_a == 3:
                    return "A"

                if count_b == 3:
                    return "B"

            if board[0][0] == 'X' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                return "A"
            if board[0][0] == 'O' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                return "B"
            if board[2][0] == 'X' and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
                return "A"
            if board[2][0] == 'O' and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
                return "B"

            count = 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] in ['X', 'O']:
                        count += 1

            if count == 9:
                return "Draw"

            return "Pending"

        board = [['.' for _ in range(3)] for _ in range(3)]
        n = len(moves)
        for i in range(n):
            if i % 2 == 0:
                board[moves[i][0]][moves[i][1]] = 'X'
            else:
                board[moves[i][0]][moves[i][1]] = 'O'

        return find_winner(board)


print(Solution().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
print(Solution().tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
print(Solution().tictactoe(
    [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
))
print(Solution().tictactoe([[0, 0], [1, 1]]))
