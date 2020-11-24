"""
Brute-force approach
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""
def can_partition(nums):
    return can_partition_recursive(nums, 0, 0, 0)


def can_partition_recursive(nums, current_index, sum1, sum2):
    
    # if all the elements are included in the sum
    if current_index == len(nums):
        return abs(sum1 - sum2)

    # recursive call after including the element in sum1
    diff1 = can_partition_recursive(nums, current_index + 1, sum1 + nums[current_index], sum2)

    # recusively call after including theelement in sum2
    diff2 = can_partition_recursive(nums, current_index + 1, sum1, sum2 + nums[current_index])

    return min(diff1, diff2)


"""
Memoization
Time Complexity - O(N * S)
Space Complexity - O(N * S + N)
"""

def can_partition_memoization(nums):
    s = sum(nums)
    dp = [[-1 for i in range(s + 1)] for j in range(len(nums))]
    return can_partition_memoization_recursive(dp, nums, 0, 0, 0)


def can_partition_memoization_recursive(dp, nums, current_index, sum1, sum2):
    
    if len(nums) == current_index:
        return abs(sum1 - sum2)

    if dp[current_index][sum1] == -1:
        diff1 = can_partition_memoization_recursive(dp, nums, current_index + 1, sum1 + nums[current_index], sum2)
        diff2 = can_partition_memoization_recursive(dp, nums, current_index + 1, sum1, sum2 + nums[current_index])

        dp[current_index][sum1] = min(diff1, diff2)

    return dp[current_index][sum1]


"""
Tabulation
Time Complexiy - O(N * S)
Space Complexity - O(N * S)
"""

def can_partition_tabulation(nums):
    s = sum(nums)
    n = len(nums)
    dp = [[False for _ in range(int(s/2) + 1)] for __ in range(len(nums))]

    # populate the sum = 0 columns, as we can always form '0' sum with an empty set
    for i in range(n):
        dp[i][0] = True
    
    # with only one number in set
    for j in range(1, int(s/2) + 1):
        dp[0][j] = nums[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s/2) + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif nums[i] <= j:
                dp[i][j] = dp[i - 1][j - nums[i]]

    sum1 = 0
    for i in range(int(s/2), -1, -1):
        if dp[len(nums) - 1][i]:
            sum1 = i
            break
    
    sum2 = s - sum1
    return abs(sum2 - sum1)







def main():
    # Bruteforce
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))

    # Memoization
    print("Can partition: " + str(can_partition_memoization([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_memoization([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_memoization([1, 3, 100, 4])))

    # Tabulation
    print("Can partition: " + str(can_partition_tabulation([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_tabulation([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_tabulation([1, 3, 100, 4])))


main()