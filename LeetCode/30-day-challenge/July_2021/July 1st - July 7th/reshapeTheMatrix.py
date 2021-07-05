"""
    Problem Link:- https://leetcode.com/problems/reshape-the-matrix/

    converting 2-d array to 1-d array
     2_d[i][j] -> one_d[i * n + j] n -> number of columns
    
    constructing a 2-d array from 1-d array
    2_d[i][j] = one_d[i * c + j] c -> number of columns in array
"""

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        return_matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                one_d = i * c + j
                return_matrix[i][j] = mat[one_d // n][one_d % n]

        return return_matrix




print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))
print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 4, c = 1))