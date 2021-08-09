from collections import defaultdict


"""
    Problem Link:- https://leetcode.com/problems/rank-transform-of-a-matrix/
"""


class DSU():
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.size[y] < self.size[x]:
            y, x = x, y
        self.size[y] += self.size[x]
        self.parent[x] = y

    def get_groups(self):
        groups = defaultdict(list)
        for x in self.parent:
            groups[self.find(x)].append(x)
        return groups


class Solution:
    def matrixRankTransform(self, matrix):
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (n + m)
        d = defaultdict(list)

        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append((i, j))

        for x in sorted(d):
            dsu = DSU()  # creating a new structure

            # initialising the dsu with row and column number as participants
            for i, j in d[x]:
                j += n  # j is shifted by n for separating rows and cols
                dsu.add(i)  # init
                dsu.add(j)  # init

            for i, j in d[x]:
                j += n  # j is shifted by n for separating rows and cols
                dsu.unite(i, j)  # unite

            # handle logic *within* a group
            for group in dsu.get_groups().values():
                max_rank = 0
                for location in group:
                    max_rank = max(max_rank, rank[location])
                for location in group:
                    rank[location] = max_rank + 1

            for i, j in d[x]:
                matrix[i][j] = rank[i]

        return matrix


print(Solution().matrixRankTransform(matrix=[[1, 2], [3, 4]]))
print(Solution().matrixRankTransform(matrix=[[7, 7], [7, 7]]))
print(Solution().matrixRankTransform(matrix=[[7, 3, 6], [1, 4, 5], [9, 8, 2]]))
