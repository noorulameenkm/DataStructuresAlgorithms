class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxOnes, length = -1, 0
        
        for end in range(len(nums)):
            
            if nums[end] == 1:
                length += 1
            
            if end == len(nums) - 1 or nums[end] == 0:
                maxOnes = max(maxOnes, length)
                length = 0
                
                
        return maxOnes
                
        
                
            
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))