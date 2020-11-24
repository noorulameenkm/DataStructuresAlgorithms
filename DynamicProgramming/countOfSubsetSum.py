"""
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""

def count_subsets(nums, sum_):
    return count_subsets_recursive(nums, sum_, 0)


def count_subsets_recursive(nums, sum_, current_index):
    if sum_ == 0:
        return 1
    
    n = len(nums)
    if n == 0 or current_index >= n:
        return 0
    
    sum1 = 0

    if nums[current_index] <= sum_:
        sum1 = count_subsets_recursive(nums, sum_ - nums[current_index], current_index + 1)


    sum2 = count_subsets_recursive(nums, sum_, current_index + 1)

    return sum1 + sum2


"""
Time Complexity - O(N * S)
Space Complexity - O(N * S + N)
"""

def count_subsets_memoization(nums, sum_):
    dp = [[-1 for _ in range(sum_ + 1)] for j in range(len(nums))]
    return count_subsets_memoization_recursive(dp, nums, sum_ , 0)

def count_subsets_memoization_recursive(dp, nums, sum_, current_index):

    if sum_ == 0:
        return 1
    
    n = len(nums)
    if n == 0 or current_index >= n:
        return 0

    sum1 = 0
    if dp[current_index][sum_] == -1:
        if nums[current_index] <= sum_:
            sum1 = count_subsets_memoization_recursive(dp, nums, sum_ - nums[current_index], current_index + 1)

        sum2 = count_subsets_memoization_recursive(dp, nums, sum_ , current_index + 1)

        dp[current_index][sum_] = sum1 + sum2
    
    return dp[current_index][sum_]



"""
Time Complexity - O(N * S)
Space Complexity - O(N * S)
"""
def count_subsets_tabulation(nums, sum_):
    dp = [[-1 for _ in range(sum_ + 1)] for j in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1
    
    for s in range(1, sum_ + 1):
        dp[0][s] = 1 if nums[0] == s else 0

    for i in range(1, len(nums)):
        for j in range(1, sum_ + 1):
            dp[i][j] = dp[i - 1][j]

            if nums[i] <= j:
                dp[i][j] += dp[i - 1][j - nums[i]]


    return dp[len(nums) - 1][sum_]


"""
Time Complexity - O(N * S)
Space Complexity - O(S)
"""

def count_subsets_space_optimized(nums, sum_):
  dp = [-1 for _ in range(sum_ + 1)]
  dp[0] = 1
  for s in range(1, sum_ + 1):
    dp[s] = 1 if nums[0] == s else 0
  
  for i in range(1, len(nums)):
    for s in range(sum_, -1, -1):
      sum1 = dp[s]

      sum2 = 0
      if nums[i] <= s:
        sum2 = dp[s - nums[i]]
      
      dp[s] = sum1 + sum2


  return dp[sum_]



def main():
    # BruteForce
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))

    # Memoization
    print("Total number of subsets " + str(count_subsets_memoization([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_memoization([1, 2, 7, 1, 5], 9)))

    # Tabulation
    print("Total number of subsets " + str(count_subsets_tabulation([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_tabulation([1, 2, 7, 1, 5], 9)))

    # Space Optimized
    print("Total number of subsets " + str(count_subsets_space_optimized([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_space_optimized([1, 2, 7, 1, 5], 9)))


main()