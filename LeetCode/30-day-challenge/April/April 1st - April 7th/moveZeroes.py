class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums)-1):
            if nums[i] == 0:
        
                if k == -1:
                    k = i + 1
                else:
                    k = k + 1 
            
                while k < len(nums) and nums[k] == 0:
                    k = k + 1 

                if k < len(nums):
                    temp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = temp
                else:
                    break
        
soln = Solution()
arr = [0,0,3,4,0,0,5,7]
print('array before moving zeroes ', arr)
soln.moveZeroes(arr)
print('array after moving zeroes ', arr)
