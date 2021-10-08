"""
Problem Link:- https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Node:
    def __init__(self, c, end=False):
        self.c = c  # current character
        self.child = {}  # 'x': Node()
        self.end = end  # is this character the last or not


class Trie:

    def __init__(self):
        self.root = Node('#')

    def insert(self, word: str) -> None:
        self.curr = self.root
        for c in word:
            if c not in self.curr.child:
                self.curr.child[c] = Node(c)
            self.curr = self.curr.child[c]
        self.curr.end = True

    def search(self, word: str) -> bool:
        self.curr = self.root
        for c in word:
            if c in self.curr.child:
                self.curr = self.curr.child[c]
            else:
                return False

        return self.curr.end

    def startsWith(self, prefix: str) -> bool:
        self.curr = self.root
        for c in prefix:
            if c in self.curr.child:
                self.curr = self.curr.child[c]
            else:
                return False

        return True
