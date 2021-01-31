"""
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""
def longestSumIncreasingSubsequence(arr):
    return longestSumIncreasingSubsequence_recursive(arr, 0, -1)


def longestSumIncreasingSubsequence_recursive(arr, index, previous):
    if index >= len(arr):
        return 0
    
    included, notIncluded = 0, 0
    if previous == -1 or arr[index] > arr[previous]:
        included = arr[index] + longestSumIncreasingSubsequence_recursive(arr, index + 1, index)
    
    notIncluded = longestSumIncreasingSubsequence_recursive(arr, index + 1, previous)


    return max(included, notIncluded)


"""
Time Complexity - O(N ^ 2)
Space Complexity - o(N ^ 2 + N)
"""
def longestSumIncreasingSubsequence_memoization(arr):
    dp = [[-1 for i in range(len(arr) + 1)] for j in range(len(arr))]
    return longestSumIncreasingSubsequence_memoization_recursive(dp, arr, 0, -1)


def longestSumIncreasingSubsequence_memoization_recursive(dp, arr, index, previous):
    if index >= len(arr):
        return 0

    if dp[index][previous + 1] == -1:
        included, notIncluded = 0, 0

        if previous == -1 or arr[index] > arr[previous]:
            included = arr[index] + longestSumIncreasingSubsequence_memoization_recursive(dp, arr, index + 1, index)

        notIncluded = longestSumIncreasingSubsequence_memoization_recursive(dp, arr, index + 1, previous)

        dp[index][previous + 1] = max(included, notIncluded)
    
    return dp[index][previous + 1]


"""
Time Complexity - O(N ^ 2)
Space complexity - O(N)
"""
def longestSumIncreasingSequence_tabulation(arr):
    dp = [0 for i in range(len(arr))]
    maxSum = arr[0]
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]
        
        maxSum = max(maxSum, dp[i])
    
    return maxSum


def main():
    # Approach 1
    print(longestSumIncreasingSubsequence([4, 1, 2, 6, 10, 1, 12]))
    print(longestSumIncreasingSubsequence([-4, 10, 3, 7, 15]))

    # Approach 2
    print(longestSumIncreasingSubsequence_memoization([4, 1, 2, 6, 10, 1, 12]))
    print(longestSumIncreasingSubsequence_memoization([-4, 10, 3, 7, 15]))

    # Approach 3
    print(longestSumIncreasingSequence_tabulation([4, 1, 2, 6, 10, 1, 12]))
    print(longestSumIncreasingSequence_tabulation([-4, 10, 3, 7, 15]))


main()