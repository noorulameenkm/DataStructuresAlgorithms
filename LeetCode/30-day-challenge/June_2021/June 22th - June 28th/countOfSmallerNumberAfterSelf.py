"""
    Problem Link:- https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""

from bisect import bisect_left

class Solution:
    def countSmaller(self, nums):
        
        def update(BIT, n_, index):
            
            while index <= n_:
                BIT[index] += 1
                
                index += (index & -index)
            
        def get_sum(BIT, index):
            
            sum_ = 0
            while index > 0:
                sum_ += BIT[index]
                
                index -= (index & -index)
            
            return sum_
            
            
        n = len(nums)
        result = [0] * n
        BIT = [0] * (n + 1)
        
        temp = [num for num in nums]
        temp.sort()
        for i in range(n):
            nums[i] = bisect_left(temp, nums[i]) + 1
        
        
        for i in range(n - 1, -1, -1):
            result[i] = get_sum(BIT, nums[i] - 1)
            update(BIT, n, nums[i])
        
        return result



print(Solution().countSmaller(nums = [5,2,6,1]))
print(Solution().countSmaller(nums = [-1]))
print(Solution().countSmaller(nums = [-1, -1]))

        
        