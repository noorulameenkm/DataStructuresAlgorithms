"""
    Problem Link:- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums_, target, type_):
            left, right = 0, len(nums_) - 1
            index = -1
            while left <= right:
                
                mid = left + (right - left) // 2
                
                if target < nums[mid]:
                    right = mid - 1
                    continue
                
                if target > nums[mid]:
                    left = mid + 1
                    continue
                
                index = mid
                if type_ == 'L':
                    right = mid - 1
                    continue
                
                if type_ == 'U':
                    left = mid + 1
                    continue
            
            return index
        
        
        lower, upper = binary_search(nums, target, 'L'), binary_search(nums, target, 'U')
        return [lower, upper]



print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))
print(Solution().searchRange(nums = [], target = 0))