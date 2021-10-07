from typing import List


"""
Problem Link:- https://leetcode.com/problems/word-search/
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(x, y, i):
            if i == len(word):
                return True

            if not (0 <= x < m and 0 <= y < n):
                return False

            if board[x][y] != word[i]:
                return False

            if board[x][y] == ' ':
                return False

            board[x][y] = ' '
            temp = search(x + 1, y, i + 1) or search(x - 1, y, i + 1) or \
                search(x, y + 1, i + 1) or search(x, y - 1, i + 1)
            board[x][y] = word[i]
            return temp

        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if search(x, y, 0):
                        return True

        return False


print(Solution().exist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    word="SEE"
))
print(Solution().exist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    word="ABCB"
))
print(Solution().exist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    word="ABCCED"
))
