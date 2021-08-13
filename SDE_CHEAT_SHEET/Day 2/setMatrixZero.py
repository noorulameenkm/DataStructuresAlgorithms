"""
    Problem Link:- https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for i in range(m):
                matrix[row][i] = 0

        for col in cols:
            for i in range(n):
                matrix[i][col] = 0


def setZeroes2(matrix):
    n, m = len(matrix), len(matrix[0])

    del_first_row = False
    del_first_col = False

    for i in range(n):
        if matrix[i][0] == 0:
            del_first_row = True
            break

    for i in range(m):
        if matrix[0][i] == 0:
            del_first_col = True
            break

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 2
                matrix[0][j] = 2

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 2 or matrix[0][j] == 2:
                matrix[i][j] = 0

    for i in range(n):
        if matrix[i][0] > 1 or del_first_row:
            matrix[i][0] = 0

    for i in range(m):
        if matrix[0][i] > 1 or del_first_col:
            matrix[0][i] = 0

    return matrix


def setZeroes3(matrix):
    rowz = 0
    colz = [0] * len(matrix[0])

    for i in range(len(matrix)):
        p = 0
        rowz = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if p == 0:
                    rowz = 1
                    p = 1
                if colz[j] != 1:
                    colz[j] = 1
                    if i != 0:
                        k = i - 1
                        while k >= 0:
                            matrix[k][j] = 0
                            k -= 1

            if colz[j] == 1:
                matrix[i][j] = 0

        if rowz == 1:
            matrix[i] = [0] * len(matrix[0])

    return matrix


def setZeroes4(matrix):
    m, n = len(matrix), len(matrix[0])

    def setNone(i_, j_):

        for k in range(n):
            if matrix[i_][k] != 0 or (matrix[i_][k] == 0 and k == j_):
                matrix[i_][k] = None

        for k in range(m):
            if matrix[k][j_] != 0:
                matrix[k][j_] = None

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                setNone(i, j)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] is None:
                matrix[i][j] = 0


def main():
    # First Approach
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f'Before Setting Zeroes: {matrix}')
    Solution().setZeroes(matrix)
    print(f'After Setting Zeroes: {matrix}')

    # Second Approach
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f'Before Setting Zeroes: {matrix}')
    setZeroes2(matrix)
    print(f'After Setting Zeroes: {matrix}')

    # Third Approach
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f'Before Setting Zeroes: {matrix}')
    setZeroes3(matrix)
    print(f'After Setting Zeroes: {matrix}')

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f'Before Setting Zeroes: {matrix}')
    setZeroes4(matrix)
    print(f'After Setting Zeroes: {matrix}')

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(f'Before Setting Zeroes: {matrix}')
    setZeroes4(matrix)
    print(f'After Setting Zeroes: {matrix}')


main()
