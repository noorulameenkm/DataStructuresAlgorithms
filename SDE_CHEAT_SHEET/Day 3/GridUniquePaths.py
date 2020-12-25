def findUniquePaths(m, n):
    current_i, current_j = 0, 0
    result = [0]

    countUniquePaths(current_i, current_j, m, n, result)

    return result[0]



def countUniquePaths(current_i, current_j, m, n, result):
    if current_i >= 0 and current_j >= 0 and current_i < m and current_j < n:
        if current_i == m - 1 and current_j == n - 1:
            result[0] += 1
            return
        
        countUniquePaths(current_i + 1, current_j, m, n, result)
        countUniquePaths(current_i, current_j + 1, m, n, result)
    
    return


def findUniquePaths2(m, n):
    current_i = current_j = 0
    return countUniquePaths2(current_i, current_j, m, n)


def countUniquePaths2(i, j, m, n):
    if i >= 0 and j >= 0 and i < m and j < n:
        if i == m - 1 and j == n - 1:
            return 1

        countDown = countUniquePaths2(i + 1, j, m, n)
        countRight = countUniquePaths2(i, j + 1, m, n)
        return countDown + countRight
    else:
        return 0

def findUniquePaths3(m, n):
    i, j = 0, 0
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    return countUniquePaths3(dp, i, j, m, n)


def countUniquePaths3(dp, i, j, m, n):
    if i >= 0 and i < m and j >= 0 and j < n:
        if i == m - 1 and j == n - 1:
            return 1
        
        if dp[i][j] == -1:
            down = countUniquePaths3(dp, i + 1, j, m, n)
            right = countUniquePaths3(dp, i, j + 1, m, n)

            dp[i][j] = down + right

        return dp[i][j]
    else:
        return 0


def findUniquePaths4(m, n):
    N = m + n - 2
    R = m - 1

    res = 1.0
    for i in range(1, R + 1):
        res = res * (N - R + i) / i

    return int(res)


def main():
    # First Approach    
    print(findUniquePaths(3, 7))
    print(findUniquePaths(3, 2))
    print(findUniquePaths(7, 3))
    print(findUniquePaths(3, 3))
    # print(findUniquePaths(23, 12))

    # Second Approach    
    print(findUniquePaths2(3, 7))
    print(findUniquePaths2(3, 2))
    print(findUniquePaths2(7, 3))
    print(findUniquePaths2(3, 3))
    # print(findUniquePaths2(23, 12))

    # Third Approach    
    print(findUniquePaths3(3, 7))
    print(findUniquePaths3(3, 2))
    print(findUniquePaths3(7, 3))
    print(findUniquePaths3(3, 3))
    print(findUniquePaths3(23, 12))

    # Fourth Approach    
    print(findUniquePaths4(3, 7))
    print(findUniquePaths4(3, 2))
    print(findUniquePaths4(7, 3))
    print(findUniquePaths4(3, 3))
    print(findUniquePaths4(23, 12))

main()



    

