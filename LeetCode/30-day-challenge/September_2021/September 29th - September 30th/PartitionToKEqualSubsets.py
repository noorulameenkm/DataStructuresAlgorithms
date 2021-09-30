from typing import List


"""
Problem Link:- https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_ = sum(nums)
        if len(nums) < k or sum_ % k != 0:
            return False

        sum_needed = sum_ // k
        visited = [False] * len(nums)

        def can_partition(nums, visited, k_, start, curr_sum):
            if k_ == 0:
                return True

            if curr_sum > sum_needed:
                return False

            if curr_sum == sum_needed:
                return can_partition(nums, visited, k_ - 1, 0, 0)

            for i in range(start, len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                if can_partition(nums, visited, k_, i + 1, curr_sum + nums[i]):
                    return True
                visited[i] = False

            return False

        return can_partition(nums, visited, k, 0, 0)


print(Solution().canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
print(Solution().canPartitionKSubsets(nums=[1, 2, 3, 4], k=3))
