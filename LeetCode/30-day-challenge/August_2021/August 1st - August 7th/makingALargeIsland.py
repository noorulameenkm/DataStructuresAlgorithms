from collections import deque


def make_a_large_island(grid):
    n = len(grid)

    visited = [[False for _ in range(n)] for _ in range(n)]
    zeroes = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                zeroes.append((i, j))

    if len(zeroes) == 0:
        return n * n

    def bfs(zero_loc):
        queue = deque([])
        area = 0
        start_, end_ = zero_loc
        grid[start_][end_] = 1
        queue.append((start_, end_))
        visited[start_][end_] = True
        while len(queue) > 0:
            loc_i, loc_j = queue.popleft()
            if grid[loc_i][loc_j] == 1:
                area += 1

                if loc_j + 1 < n and not visited[loc_i][loc_j + 1] and grid[loc_i][loc_j + 1] == 1:
                    queue.append((loc_i, loc_j + 1))
                    visited[loc_i][loc_j + 1] = True

                if loc_j - 1 >= 0 and not visited[loc_i][loc_j - 1]\
                   and grid[loc_i][loc_j - 1] == 1:
                    queue.append((loc_i, loc_j - 1))
                    visited[loc_i][loc_j - 1] = True

                if loc_i + 1 < n and not visited[loc_i + 1][loc_j] and grid[loc_i + 1][loc_j] == 1:
                    queue.append((loc_i + 1, loc_j))
                    visited[loc_i + 1][loc_j] = True

                if loc_i - 1 >= 0 and not visited[loc_i - 1][loc_j]\
                   and grid[loc_i - 1][loc_j] == 1:
                    queue.append((loc_i - 1, loc_j))
                    visited[loc_i - 1][loc_j] = True

        grid[start_][end_] = 0
        return area

    def restructure_visited():
        for i in range(n):
            for j in range(n):
                visited[i][j] = False

    max_area = 0
    for k in range(len(zeroes)):
        island_area = bfs(zeroes[k])
        max_area = max(max_area, island_area)
        restructure_visited()

    return max_area


print(make_a_large_island(grid=[[1, 0], [0, 1]]))
print(make_a_large_island(grid=[[1, 1], [1, 0]]))
print(make_a_large_island(grid=[[1, 1], [1, 1]]))


def make_large_islands_2(grid):
    n = len(grid)
    island_area = {}

    def dfs(i_, j_):
        if i_ >= 0 and i_ < n and j_ >= 0 and j_ < n and grid[i_][j_] == 1:
            grid[i_][j_] = current_id
            island_area[current_id] += 1
            dfs(i_ + 1, j_)
            dfs(i_ - 1, j_)
            dfs(i_, j_ + 1)
            dfs(i_, j_ - 1)

    current_id = 2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                island_area[current_id] = 0
                dfs(i, j)
                current_id += 1

    max_area = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                area = 1
                visited = []
                if i + 1 < n and grid[i + 1][j] > 0 and grid[i + 1][j] not in visited:
                    area += island_area[grid[i + 1][j]]
                    visited.append(grid[i + 1][j])

                if i - 1 >= 0 and grid[i - 1][j] > 0 and grid[i - 1][j] not in visited:
                    area += island_area[grid[i - 1][j]]
                    visited.append(grid[i - 1][j])

                if j + 1 < n and grid[i][j + 1] > 0 and grid[i][j + 1] not in visited:
                    area += island_area[grid[i][j + 1]]
                    visited.append(grid[i][j + 1])

                if j - 1 >= 0 and grid[i][j - 1] > 0 and grid[i][j - 1] not in visited:
                    area += island_area[grid[i][j - 1]]
                    visited.append(grid[i][j - 1])

                max_area = max(max_area, area)

    if max_area > 0:
        return max_area

    return n * n


print(make_large_islands_2(grid=[[1, 0], [0, 1]]))
print(make_large_islands_2(grid=[[1, 1], [1, 0]]))
print(make_large_islands_2(grid=[[1, 1], [1, 1]]))
