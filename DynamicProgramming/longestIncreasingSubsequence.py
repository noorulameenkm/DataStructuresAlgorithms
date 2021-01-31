
"""
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""

def longestIncreasingSubsequence(arr):
    return longestIncreasingSubsequence_recursive(arr, 0, -1)


def longestIncreasingSubsequence_recursive(arr, index, previous):
    if index >= len(arr):
        return 0
    
    included, notIncluded = 0, 0
    if previous == -1 or arr[index] > previous:
        included = 1 + longestIncreasingSubsequence_recursive(arr, index + 1, arr[index])
    
    notIncluded = longestIncreasingSubsequence_recursive(arr, index + 1, previous)

    return max(included, notIncluded)


"""
Time Complexity - O(N ^ 2)
Space Complexity - O(N^2 + N)
"""
def longestIncreasingSubsequence_memoization(arr):
    dp = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr))]
    return longestIncreasingSubsequence_memoization_recursive(dp, arr, 0, -1)


def longestIncreasingSubsequence_memoization_recursive(dp, arr, index, previous):
    if index >= len(arr):
        return 0

    if dp[index][previous + 1] == -1:
        included, notIncluded = 0, 0

        if previous == -1 or arr[index] > arr[previous]:
            included = 1 + longestIncreasingSubsequence_memoization_recursive(dp, arr, index + 1, index)

        notIncluded = longestIncreasingSubsequence_memoization_recursive(dp, arr, index + 1, previous)
    
        dp[index][previous + 1] = max(included, notIncluded)
    
    return dp[index][previous + 1]


"""
Time Complexity - O(N ^ 2)
Space complexity - O(N)
"""
def find_LIS_tabulation(arr):
    dp = [0 for _ in range(len(arr))]
    dp[0] = 1
    n = len(arr)
    maxLength = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])

    return maxLength




def main():
    # Approach1
    print(longestIncreasingSubsequence([4,2,3,6,10,1,12]))
    print(longestIncreasingSubsequence([-4,10,3,7,15]))

    # Approach 2
    print(longestIncreasingSubsequence_memoization([4,2,3,6,10,1,12]))
    print(longestIncreasingSubsequence_memoization([-4,10,3,7,15]))

    # Approach 3
    print(find_LIS_tabulation([4,2,3,6,10,1,12]))
    print(find_LIS_tabulation([-4,10,3,7,15]))

main()