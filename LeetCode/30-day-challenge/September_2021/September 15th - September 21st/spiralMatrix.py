from typing import List


"""
    Problem Link:- https://leetcode.com/problems/spiral-matrix/
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        startRow, endRow, startCol, endCol = 0, m - 1, n - 1, 0

        while len(result) < m * n:
            for i in range(endCol, startCol + 1):
                result.append(matrix[startRow][i])

            startRow += 1

            if len(result) == m * n:
                break

            for i in range(startRow, endRow + 1):
                result.append(matrix[i][startCol])

            startCol -= 1
            if len(result) == m * n:
                break

            for i in range(startCol, endCol - 1, -1):
                result.append(matrix[endRow][i])

            endRow -= 1

            if len(result) == m * n:
                break

            for i in range(endRow, startRow - 1, -1):
                result.append(matrix[i][endCol])

            endCol += 1

        return result


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
