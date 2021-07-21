from collections import deque


"""
    Problem Link:- https://leetcode.com/problems/rotting-oranges/
    Time Complexity - O(N * M)
    Space Complexity - O(N * M)
"""
def rotten_oranges(grid):
    fresh = 0
    rotten = deque([])
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten.append((i,j))
                continue
            
            if grid[i][j] == 1:
                fresh += 1
                continue
    
    if fresh == 0:
        return 0
    
    if len(rotten) == 0:
        return -1
    
    def is_valid(i_, j_):
        return i_ >= 0 and i_ < m and j_ >= 0 and j_ < n

    def bfs(i_, j_):
        count = 0
        if is_valid(i_ + 1, j_) and grid[i_ + 1][j_] == 1:
            count += 1
            rotten.append((i_ + 1, j_))
            grid[i_ + 1][j_] = 2
        
        if is_valid(i_ - 1, j_) and grid[i_ - 1][j_] == 1:
            count += 1
            rotten.append((i_ - 1, j_))
            grid[i_ - 1][j_] = 2
        
        if is_valid(i_, j_ + 1) and grid[i_][j_ + 1] == 1:
            count += 1
            rotten.append((i_, j_ + 1))
            grid[i_][j_ + 1] = 2
        
        if is_valid(i_, j_ - 1) and grid[i_][j_ - 1] == 1:
            count += 1
            rotten.append((i_, j_ - 1))
            grid[i_][j_ - 1] = 2
        
        return count
    
    time = 0
    while len(rotten) > 0:
        length = len(rotten)
        sum_ = 0
        for _ in range(length):
            i, j = rotten.popleft()
            count = bfs(i, j)
            sum_ += count

        if sum_ > 0:
            fresh -= sum_
            time += 1

    if fresh > 0:
        return -1
    
    return time




print(rotten_oranges(grid = [[2,1,1],[1,1,0],[0,1,1]]))
print(rotten_oranges(grid = [[2,1,1],[0,1,1],[1,0,1]]))
print(rotten_oranges(grid = [[0,2]]))
