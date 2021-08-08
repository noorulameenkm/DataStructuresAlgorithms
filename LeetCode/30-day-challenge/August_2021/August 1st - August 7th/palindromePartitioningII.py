"""
 Problem Link:- https://leetcode.com/problems/palindrome-partitioning-ii/
"""

from functools import lru_cache


def palindrome_partitioning_2(s):
    dp = build_matrix(s)
    n = len(s)
    if n <= 1:
        return 0

    cuts = [0 for _ in range(n)]
    for i in range(n):
        cut = i
        for j in range(i + 1):
            if dp[j][i]:
                cut = min(cut, 0 if j == 0 else cuts[j - 1] + 1)

        cuts[i] = cut

    return cuts[-1]


"""
a b b c
"""


def build_matrix(string):
    dp = [[False for _ in range(len(string))] for _ in range(len(string))]
    n = len(string)
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if string[i] == string[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    return dp


print(palindrome_partitioning_2(s="aab"))
print(palindrome_partitioning_2(s="ab"))


def palindrome(string):
    return string == string[::-1]


def palindrome_partitioning_2_recursive(s):
    n = len(s)

    @lru_cache(None)
    def recursive(start):
        if start >= n:
            return 0

        min_cuts = float('inf')
        for end in range(start + 1, n + 1):
            if palindrome(s[start: end]):
                cuts = 1 + recursive(end)
                min_cuts = min(min_cuts, cuts)

        return min_cuts

    return recursive(0) - 1


print(palindrome_partitioning_2_recursive(s="aab"))
print(palindrome_partitioning_2_recursive(s="ab"))
