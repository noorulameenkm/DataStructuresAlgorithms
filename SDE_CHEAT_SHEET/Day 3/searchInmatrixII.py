class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        n, m = len(matrix), len(matrix[0])
        
        i, j = 0, m - 1
        
        while i < n and j < m and i >= 0 and j >= 0:
            if matrix[i][j] == target:
                return True
            
            if target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        
        return False

def searchInMatrix(matrix, val):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == val:
                return True

    return False



def main():
    # Fisrt Approach
    print(searchInMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    print(searchInMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
    
    # Second Approach
    print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))

main()
    
    
        