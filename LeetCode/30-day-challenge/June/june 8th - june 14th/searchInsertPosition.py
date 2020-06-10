class Solution:
    def searchInsert(self, nums, target):
        index  = -1
        start, end = 0, len(nums) - 1
        found = False
        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                index = mid
                found = True
                break
            if target > nums[mid]:
                start = mid + 1
                
            
            if target < nums[mid]:
                end = mid - 1
            
        if not found:
            if nums[start] == target:
                index = start
            elif nums[start] - target < 0:
                index = start + 1
            elif nums[start] - target > 0:
                index = start if start != 0 else 0
        
        return index
                
    
print(f'Solution for [1,3,5,6], 5 is {Solution().searchInsert([1,3,5,6], 5)}')
print(f'Solution for [1,3,5,6], 2 is {Solution().searchInsert([1,3,5,6], 2)}')