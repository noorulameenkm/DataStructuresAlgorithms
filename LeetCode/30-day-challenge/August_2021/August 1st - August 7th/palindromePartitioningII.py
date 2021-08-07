"""
 Problem Link:- https://leetcode.com/problems/palindrome-partitioning-ii/
"""


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
