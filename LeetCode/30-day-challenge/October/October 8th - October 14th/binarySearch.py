class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
            
        return -1

print(Solution().search([-1,0,3,5,9,12], 9))
                
                
        