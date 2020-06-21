class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board == [] or len(board[0]) <= 2:
            return
        
        row, col = len(board), len(board[0])
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = '-'
        
        
        for j in range(col):
            fill(board, 0, j, row, col)
            fill(board, row - 1, j, row, col)
        
        for i in range(row):
            fill(board, i, 0, row, col)
            fill(board, i, col - 1, row, col)
            
        for i in range(row):
            for j in range(col):
                if board[i][j] == '-':
                    board[i][j] = 'X'
        
        
        

def fill(board, i, j, row, col):
    if i < 0 or j < 0 or i >= row or j >= col:
        return
    
    if board[i][j] != '-':
        return
    
    
    board[i][j] = 'O'
    
    fill(board, i, j + 1, row, col)
    fill(board, i, j - 1, row, col)
    fill(board, i + 1, j, row, col)
    fill(board, i - 1, j, row, col)




board = [  
           ['X', 'X', 'X', 'X'],
           ['X', 'O', 'O', 'X'],
           ['X', 'X', 'O', 'X'],
           ['X', 'O', 'X', 'X']
        ]


print('Board before executing', board)
Solution().solve(board)
print('Board after executing', board)

    
                    
        