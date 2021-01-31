


def no_of_ways(n):
    arr = [0 for i in range(n + 1)]
    arr[0] = arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]


"""
Time Complexity - O(3 ^ N)
Space Complexity - O(N)
"""
def number_of_ways(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    n_1 = number_of_ways(n - 1)
    n_2 = number_of_ways(n - 2)
    n_3 = number_of_ways(n - 3)

    return n_1 + n_2 + n_3


"""
Time Complexity - O(N)
Space complexity - O(N)
"""
def count_ways_memoization(n):
    dp = [0 for _ in range(n + 1)]

    return count_ways_memoization_recursive(dp, n)

def count_ways_memoization_recursive(dp, n):
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2

    if dp[n] == 0:

        c_1 = number_of_ways(n - 1)
        c_2 = number_of_ways(n - 2)
        c_3 = number_of_ways(n - 3)
        dp[n] = c_1 + c_2 + c_3
    
    return dp[n]



"""
Time Complexity - O(N)
Space complexity - O(N)
"""
def number_of_ways_tabulation(n):

    dp = [1, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    return dp[n]




def main():
    # Approach 1
    print(no_of_ways(2))
    print(no_of_ways(4))

    # Approach 2
    print(number_of_ways(3))
    print(number_of_ways(4))
    print(number_of_ways(5))

    # Approach 3
    print(count_ways_memoization(3))
    print(count_ways_memoization(4))
    print(count_ways_memoization(5))

    # Approach 4
    print(number_of_ways_tabulation(3))
    print(number_of_ways_tabulation(4))
    print(number_of_ways_tabulation(5))
    
main()