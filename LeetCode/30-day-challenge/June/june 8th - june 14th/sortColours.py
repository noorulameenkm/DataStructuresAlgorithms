class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        firstPtr = currPtr = 0
        
        secondPtr = len(nums) - 1
        
        while currPtr <= secondPtr:
            if nums[currPtr] == 0:
                nums[firstPtr], nums[currPtr] = nums[currPtr], nums[firstPtr]
                firstPtr += 1
                currPtr += 1
            elif nums[currPtr] == 2:
                nums[secondPtr], nums[currPtr] = nums[currPtr], nums[secondPtr]
                secondPtr -= 1
            else:
                currPtr += 1



arr = [0,1,2,0,1,0,2,1,2]