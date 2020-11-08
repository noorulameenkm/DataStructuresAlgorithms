

# Recursive approach ---------------------------------

"""
Time Complexity - O(2^n)
Space Complexity - O(n)
"""

def can_partition(nums):
  # TODO: Write your code here
  if len(nums) == 0:
    return False

  S = sum(nums)

  if S % 2 != 0:
    return False

  return check_partitioning(nums, S / 2, 0)


def check_partitioning(nums, sum_, index):
  if sum_ == 0:
    return True
  
  n = len(nums)

  if n == 0 or index >= n:
    return False

  # recursive call after choosing the number at the `currentIndex`
  # if the number at `currentIndex` exceeds the sum, we shouldn't process this
  if nums[index] <= sum_:
    if check_partitioning(nums, sum_ - nums[index], index + 1):
      return True
  
  # recursive call after excluding the number at the 'currentIndex'
  return check_partitioning(nums, sum_, index + 1)

#-----------------------------------------------------

# Memoization -------------------------------------
"""
Time Complexity - O(N * S)
Space Complexity - O(N * S)
"""

def check_partitioning_memoization(nums):
    S, length = sum(nums), len(nums)

    if length == 0 or S % 2 != 0:
        return False

    dp = [[-1 for i in range(S + 1)] for j in range(length)]

    return True if can_partition_memoization(dp, nums, int(S / 2), 0) == 1 else False


def can_partition_memoization(dp, nums, sum_, index):
    if sum_ == 0:
        return 1
    
    if index >= len(nums):
        return 0

    if dp[index][sum_] != -1:
        return dp[index][sum_]


    included = 0

    if nums[index] <= sum_:
        included = can_partition_memoization(dp, nums, sum_ - nums[index], index + 1)
        
    notIncluded = can_partition_memoization(dp, nums, sum_, index + 1)
    
    dp[index][sum_] = 1 if included == 1 or notIncluded == 1 else 0

    return dp[index][sum_]

#--------------------------------------------------

# Tabulation --------------------------------------
"""
Time complexity - O(N * S)
Space complexity - O(N * S)
"""

def can_partitioning_tabulation(nums):
    if len(nums) == 0 or sum(nums) % 2 != 0:
        return False

    S = int(sum(nums) / 2)

    dp = [[False for i in range(S + 1)] for j in range(len(nums))]

    # populate the sum=0 column, as we can always have '0' sum without including 
    # any element
    for i in range(len(nums)):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for s in range(1, S+1):
        if nums[0] == s:
            dp[0][s] = True

    # process all subsets for all sums
    for i in range(1, len(nums)):
        for s in range(1, S + 1):

            included = False
            if nums[i] <= s:
                included = dp[i - 1][s - nums[i]]

            notIncluded = dp[i - 1][s]

            dp[i][s] = included or notIncluded

    return dp[len(nums) - 1][S]

#--------------------------------------------------


def main():
    # Recursive
    print(can_partition([1, 2, 3, 4]))
    print(can_partition([1, 1, 3, 4, 7]))
    print(can_partition([2, 3, 4, 6]))
    # Memoization
    print(check_partitioning_memoization([1, 2, 3, 4]))
    print(check_partitioning_memoization([1, 1, 3, 4, 7]))
    print(check_partitioning_memoization([2, 3, 4, 6]))
    # Tabulation
    print(can_partitioning_tabulation([1, 2, 3, 4]))
    print(can_partitioning_tabulation([1, 1, 3, 4, 7]))
    print(can_partitioning_tabulation([2, 3, 4, 6]))

main()