"""
    Problem Link:- https://leetcode.com/problems/partition-array-into-disjoint-intervals/
"""

def partition_array(nums):
    n = len(nums)
    left_max = [0 for _ in range(n)]
    right_min = [0 for _ in range(n)]

    for i in range(n):
        if i == 0:
            left_max[i] = nums[i]
            continue

        left_max[i] = max(nums[i], left_max[i - 1])
    
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            right_min[i] = nums[i]
            continue

        right_min[i] = min(nums[i], right_min[i + 1])

    for i in range(1, n):
        if left_max[i - 1] <= right_min[i]:
            return i



def partition_array_2(nums):
    max_until_i = nums[0]
    max_in_left_partition = nums[0]
    partition_id = 0

    for i in range(1, len(nums)):
        max_until_i = max(max_until_i, nums[i])
        if nums[i] < max_in_left_partition:
            max_in_left_partition = max_until_i
            partition_id = i

    return partition_id + 1


# First Approach
print(partition_array(nums = [5,0,3,8,6]))
print(partition_array(nums = [1,1,1,0,6,12]))

# Second Approach 
print(partition_array_2(nums = [5,0,3,8,6]))
print(partition_array_2(nums = [1,1,1,0,6,12]))