"""
    Problem Link:- https://leetcode.com/problems/out-of-boundary-paths/
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memory = {}
        MOD = pow(10, 9) + 7

        def get_memo_key(row_, col_, moves_):
            return f"{row_}:{col_}:{moves_}"
        
        def find_paths_recursive(m_, n_, moves, row, col):
            if moves < 0:
                return 0
            
            if row == m_ or col == n_ or row < 0 or col < 0:
                return 1
            
            key = get_memo_key(row, col, moves)
            if key in memory:
                return memory[key]
            
            left = find_paths_recursive(m_, n_, moves - 1, row, col - 1)
            right = find_paths_recursive(m_, n_, moves - 1, row, col + 1)
            up = find_paths_recursive(m_, n_, moves - 1, row - 1, col)
            down = find_paths_recursive(m_, n_, moves - 1, row + 1, col)
            
            total = (left + right + up + down) % MOD
            memory[key] = total
            return memory[key]
        
        
        return find_paths_recursive(m, n, maxMove, startRow, startColumn)
            


print(Solution().findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
print(Solution().findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))