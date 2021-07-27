"""
    Problem Link:- https://leetcode.com/problems/3sum-closest/
"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[len(nums) - 1]
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
                    
        return closest_sum


print(Solution().threeSumClosest([-2, 0, 1, 2], 2))
print(Solution().threeSumClosest([-3, -1, 1, 2], 1))
print(Solution().threeSumClosest([1, 0, 1, 1], 100))
print(Solution().threeSumClosest([-1,2,1,-4], 1))