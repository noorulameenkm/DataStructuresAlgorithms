class Solution:
    def fourSum(self, nums, target):
        fourbles = []
        nums.sort()
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
            
                searchPair(nums[i], nums[j], nums, j + 1 ,target, fourbles)
                
        return fourbles
                
                

def searchPair(num1, num2, nums, left, target, fourbles):
    right = len(nums) - 1
    
    while left < right:
        sum_ = num1 + num2 + nums[left] + nums[right]
        
        if sum_ > target:
            right -= 1
        elif sum_ < target:
            left += 1
        else:
            fourbles.append([num1, num2, nums[left], nums[right]])
            
            left += 1
            right -= 1
            
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            
            while right > left and nums[right] == nums[right + 1]:
                right -= 1
                
    

print(Solution().fourSum([1,0,-1,0,-2,2], 0))