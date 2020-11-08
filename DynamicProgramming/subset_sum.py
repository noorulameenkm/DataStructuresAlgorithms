
# Recursive ------------------------------------------------
"""
Time Complexity - O(2 ^ n)
Space complexity - O(n)
"""

def subset_sum_recursive(nums, sum_):
    if sum_ < 0 or len(nums) == 0:
        return False

    return subset_sum_recursive_(nums, sum_, 0)


def subset_sum_recursive_(nums, sum_, index):
    if sum_ == 0:
        return True

    if index >= len(nums):
        return False

    included = 0
    if nums[index] <= sum_:
        included = subset_sum_recursive_(nums, sum_ - nums[index], index + 1)

    notIncluded = subset_sum_recursive_(nums, sum_, index + 1)

    return included or notIncluded

#----------------------------------------------------------------


# Memoization----------------------------------------------------
"""
Time Complexity - O(N * S)
Space complexity - O(N * S)
"""

def subset_sum_memoization(nums, sum_):
    if sum_ < 0 or len(nums) == 0:
        return False

    dp = [[-1 for i in range(sum_ + 1)] for j in range(len(nums))]

    return True if subset_sum_memoization_(dp, nums, sum_, 0) == 1 else False



def subset_sum_memoization_(dp, nums, sum_, index):
    if sum_ == 0:
        return 1

    if index >= len(nums):
        return 0

    if dp[index][sum_] != -1:
        return dp[index][sum_]

    included = 0

    if nums[index] <= sum_:
        included = subset_sum_memoization_(dp, nums, sum_ - nums[index], index + 1)

    notIncluded = subset_sum_memoization_(dp, nums, sum_, index + 1)

    dp[index][sum_] = 1 if included == 1 or notIncluded == 1 else 0

    return dp[index][sum_]    
    
#-----------------------------------------------------------------

# Tabulation------------------------------------------------------
"""
Time Complexity - O(N * S)
Space Complexity - O(N * S)
"""

def subset_sum_tabulation(nums, sum_):
    if sum_ < 0 or len(nums) == 0:
        return False

    n = len(nums)

    dp = [[False for i in range(sum_ + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    for s in range(1, sum_ + 1):
        dp[0][s] = nums[0] == s

    for i in range(1, n):
        for s in range(1, sum_ + 1):

            included = False

            if nums[i] <= s:
                included = dp[i - 1][s - nums[i]]

            notIncluded = dp[i - 1][s]

            dp[i][s] = included or notIncluded
    
    return dp[n - 1][sum_]
#-----------------------------------------------------------------

# Tabulation with space optimization------------------------------

def subset_sum_tabulation_memory_optimized(nums, sum_):
   if sum_ < 0 or len(nums) == 0:
      return False

   n = len(nums)

   dp = [False for i in range(sum_ + 1)]

   for s in range(sum_ + 1):
      dp[s] = nums[0] == s

   for i in range(1, n):
      for s in range(sum_, -1, -1):
         included = False

         if nums[i] <= s:
            included = dp[s - nums[i]]
         
         notIncluded = dp[s]

         dp[s] = included or notIncluded

   return dp[sum_]


#-----------------------------------------------------------------


def main():
    # Recursive 
    print(subset_sum_recursive([1, 2, 3, 7], 6))
    print(subset_sum_recursive([1, 2, 7, 1, 5], 10))
    print(subset_sum_recursive([1, 3, 4, 8], 6))
    # Memoization 
    print(subset_sum_memoization([1, 2, 3, 7], 6))
    print(subset_sum_memoization([1, 2, 7, 1, 5], 10))
    print(subset_sum_memoization([1, 3, 4, 8], 6))
    # Tabulation
    print(subset_sum_tabulation([1, 2, 3, 7], 6))
    print(subset_sum_tabulation([1, 2, 7, 1, 5], 10))
    print(subset_sum_tabulation([1, 3, 4, 8], 6))
    # Tabulation with memory optimized 
    print(subset_sum_tabulation_memory_optimized([1, 2, 3, 7], 6))
    print(subset_sum_tabulation_memory_optimized([1, 2, 7, 1, 5], 10))
    print(subset_sum_tabulation_memory_optimized([1, 3, 4, 8], 6))



main()