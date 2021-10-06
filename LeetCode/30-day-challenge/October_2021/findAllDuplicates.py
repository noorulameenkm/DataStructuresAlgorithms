from typing import List


"""
Problem Link:- https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            x = nums[i]

            if nums[abs(x) - 1] < 0:
                ans.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1

        return ans


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDuplicates([1, 1, 2]))
print(Solution().findDuplicates([1]))
