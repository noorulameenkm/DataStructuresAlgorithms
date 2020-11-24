"""
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""

def find_longest_palindrome(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    
    if startIndex == endIndex:
        return 1

    if st[startIndex] == st[endIndex]:
        return 2 + find_LPS_length_recursive(st, startIndex + 1, endIndex - 1)
    
    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)

    return max(c1, c2)


"""
Time Complexity - O(N * N)
Space Complexity - O(N * N + N)
"""

def find_longest_palindrome_memoization(st):
    dp = [[-1 for _ in range(len(st))] for _ in range(len(st))]
    return find_LPS_length_memoization(dp, st, 0, len(st) - 1)

def find_LPS_length_memoization(dp, st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    if startIndex == endIndex:
        return 1
    
    if dp[startIndex][endIndex] == -1:
        if st[startIndex] == st[endIndex]:
            dp[startIndex][endIndex] = 2 + find_LPS_length_memoization(dp, st, startIndex + 1, endIndex - 1)
        else:
            c1 = find_LPS_length_memoization(dp, st, startIndex + 1, endIndex)
            c2 = find_LPS_length_memoization(dp, st, startIndex, endIndex - 1)

            dp[startIndex][endIndex] = max(c1, c2)


    return dp[startIndex][endIndex]


"""
Time Complexity - O(N*N)
Space Complexity - O(N*N)
"""

def find_longest_palindrome_tabulation(st):
    dp = [[0 for _ in range(len(st))] for _ in range(len(st))]
    n = len(st)
    for i in range(n):
        dp[i][i] = 1
    
    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):

            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1]
                )

    return dp[0][n - 1]


def main():
    # Bruteforce
    print(find_longest_palindrome("abdbca"))
    print(find_longest_palindrome("cddpd"))
    print(find_longest_palindrome("pqr"))

    # Memoization
    print(find_longest_palindrome_memoization("abdbca"))
    print(find_longest_palindrome_memoization("cddpd"))
    print(find_longest_palindrome_memoization("pqr"))

    # Tabulation
    print(find_longest_palindrome_tabulation("abdbca"))
    print(find_longest_palindrome_tabulation("cddpd"))
    print(find_longest_palindrome_tabulation("pqr"))

main()