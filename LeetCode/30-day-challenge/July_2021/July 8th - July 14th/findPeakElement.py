"""
    Problem Link:- https://leetcode.com/problems/find-peak-element/
"""


from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid + 1] > nums[mid]:
                start = mid + 1
            else:
                end = mid
                
        return start


print(Solution().findPeakElement(nums = [1,2,3,1]))
print(Solution().findPeakElement(nums = [1,2,1,3,5,6,4]))

