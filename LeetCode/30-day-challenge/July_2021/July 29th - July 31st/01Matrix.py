from math import inf
from collections import deque

"""
    Problem Link:- https://leetcode.com/problems/01-matrix/
"""

"""
  Maximum recursion limit exceeded
"""


def zero_one_mat(mat):
    m, n = len(mat), len(mat[0])
    result_mat = [[0 for _ in range(n)] for _ in range(m)]

    def is_valid(_i, _j):
        return _i >= 0 and _i < m and _j >= 0 and _j < n

    def dfs(i_, j_, count):
        if mat[i_][j_] == 0:
            return count

        min_ = inf

        if is_valid(i_, j_ + 1):
            right_dist = dfs(i_, j_ + 1, count + 1)
            min_ = min(min_, right_dist)

        if is_valid(i_, j_ - 1):
            left_dist = dfs(i_, j_ - 1, count + 1)
            min_ = min(min_, left_dist)

        if is_valid(i_ + 1, j_):
            down_dist = dfs(i_ + 1, j_, count + 1)
            min_ = min(min_, down_dist)

        if is_valid(i_ - 1, j_):
            up_dist = dfs(i_ - 1, j_, count + 1)
            min_ = min(min_, up_dist)

        return min_

    for i in range(m):
        for j in range(n):
            if mat[i][j] != 0:
                dist = dfs(i, j, 0)
                result_mat[i][j] = dist

    return result_mat

# print(zero_one_mat(mat = [[0,0,0],[0,1,0],[0,0,0]]))
# print(zero_one_mat(mat = [[0,0,0],[0,1,0],[1,1,1]]))


"""
    Time Complexity - O(m * n)
    BFS Approach
"""


def zero_one_matrix(mat):
    queue = deque([])
    m, n = len(mat), len(mat[0])
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = -1

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    level = 0
    while len(queue) > 0:
        level += 1

        length = len(queue)
        while length > 0:
            row, col = queue.popleft()
            for direction in directions:
                r, c = row + direction[0], col + direction[1]
                if r < 0 or c < 0 or r == m or c == n or mat[r][c] != -1:
                    continue

                mat[r][c] = level
                queue.append((r, c))

            length -= 1

    return mat


print(zero_one_matrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(zero_one_matrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
