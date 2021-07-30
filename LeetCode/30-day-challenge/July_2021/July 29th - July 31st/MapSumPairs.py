"""
    Problem Link:- https://leetcode.com/problems/map-sum-pairs/
"""


class TrieNode:
    def __init__(self):
        self.childrens = [None] * 26
        self.is_end_of_word = False
        self.value = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        root = self.root
        for char in key:
            index = self._char_to_index(char)
            if root.childrens[index] is None:
                root.childrens[index] = TrieNode()

            root = root.childrens[index]

        root.is_end_of_word = True
        root.value = val

    def sum(self, prefix):
        sum_ = [0]
        root = self.root
        for char in prefix:
            index = self._char_to_index(char)
            if root.childrens[index] is None:
                return 0
            root = root.childrens[index]

        self.recursive_sum(root, sum_)
        return sum_[0]

    def recursive_sum(self, root, sum_):
        if root.is_end_of_word:
            sum_[0] += root.value

        for i in range(26):
            if root.childrens[i] is not None:
                self.recursive_sum(root.childrens[i], sum_)

    def _char_to_index(self, char):
        return ord(char) - ord('a')


# first test case
mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))
mapSum.insert("app", 2)
print(mapSum.sum("ap"))

# second test case
mapSum = MapSum()
mapSum.insert("a", 3)
print(mapSum.sum("ap"))
mapSum.insert("b", 2)
print(mapSum.sum("a"))


class MapSum2:
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        sum_ = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                sum_ += val

        return sum_


# first test case for MapSum2
mapSum = MapSum2()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))
mapSum.insert("app", 2)
print(mapSum.sum("ap"))

# second test case for MapSum2
mapSum = MapSum2()
mapSum.insert("a", 3)
print(mapSum.sum("ap"))
mapSum.insert("b", 2)
print(mapSum.sum("a"))
