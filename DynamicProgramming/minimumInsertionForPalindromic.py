"""
Time Complexity - O(N*2)
Space Complexity - O(N*2)
"""
def minimum_insertion_palindrome(str_):
    # substracting the length of the longest palindromic subsequence
    # from the length of the string will give the minimum deletion
    return len(str_) - LPS(str_)



def LPS(str_):
    n = len(str_)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if str_[startIndex] == str_[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:
                dp[startIndex][endIndex] = max(dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

    return dp[0][n - 1]


def main():
  print(minimum_insertion_palindrome("abdbca"))
  print(minimum_insertion_palindrome("cddpd"))
  print(minimum_insertion_palindrome("pqr"))

main()