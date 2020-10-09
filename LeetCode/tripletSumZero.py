class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            searchPair(nums[i], nums, i + 1, -nums[i], triplets)
        
        return triplets
            


def searchPair(num, nums, left, target, triplets):
    right = len(nums) - 1
    
    while left < right:
        sum_ = nums[left] + nums[right]
        
        if sum_ > target:
            right -= 1
        elif sum_ < target:
            left += 1
        else:
            triplets.append([num, nums[left], nums[right]])
            left += 1
            right -= 1
            
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            
            while right > left and nums[right] == nums[right + 1]:
                right -= 1


print(Solution().threeSum([-1,0,1,2,-1,-4]))      