class Solution:
    def generateMatrix(self, n):
        start, end = 1, n * n
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        startRow, endRow, startCol, endCol = 0, n - 1, n - 1, 0
        
        while start <= end:
            
            for i in range(endCol, startCol + 1):
                matrix[startRow][i] = start
                start += 1
            
            startRow += 1
            
            if start > end:
                break
            
            for i in range(startRow, endRow + 1):
                matrix[i][startCol] = start
                start += 1
            
            startCol -= 1
            
            if start > end:
                break
            
            for i in range(startCol, endCol - 1, -1):
                matrix[endRow][i] = start
                start += 1
            
            endRow -= 1
            
            if start > end:
                break
            
            for i in range(endRow, startRow - 1, -1):
                matrix[i][endCol] = start
                start += 1
            
            endCol += 1
        
            if start > end:
                break
            
        return matrix


def main():
    print(Solution().generateMatrix(3))

main()
            
            
            
            
        