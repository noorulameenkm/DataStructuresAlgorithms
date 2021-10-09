from typing import List


"""
Problem Link:- https://leetcode.com/problems/word-search-ii/
"""


class Node:
    def __init__(self, c, end=False):
        self.c = c
        self.child = {}
        self.end = end


class Trie:
    def __init__(self):
        self.root = Node('#')

    def add_word(self, word):
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)

            curr = curr.child[c]

        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m, n = len(board), len(board[0])
        ans = set()

        def search(x, y, curr, path):

            if not (0 <= x < m and 0 <= y < n):
                return

            c = board[x][y]
            if c not in curr.child:
                return

            if curr.child[c].end:
                ans.add(path + c)

            board[x][y] = ' '
            search(x + 1, y, curr.child[c], path + c)
            search(x - 1, y, curr.child[c], path + c)
            search(x, y + 1, curr.child[c], path + c)
            search(x, y - 1, curr.child[c], path + c)
            board[x][y] = c

        trie = Trie()
        for word in words:
            trie.add_word(word)

        curr = trie.root

        for x in range(m):
            for y in range(n):
                search(x, y, curr, "")

        return list(ans)


print(Solution().findWords(
    board=[
        ["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]
    ],
    words=["oath", "pea", "eat", "rain"]
))
print(Solution().findWords(
    board=[
        ["a", "b"], ["c", "d"]
    ],
    words=["abcb"]
))
