class Solution:
    def majorityElement(self, nums):
        max_el = nums[0]
        max_el_count = 1
        
        d = {max_el: 1}
        
        for i in range(1, len(nums)):
            if d.get(nums[i], 0) == 0:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            
            
            if d[nums[i]] > max_el_count:
                max_el_count = d[nums[i]]
                max_el = nums[i]
                
        return max_el


print(f'Max Count Element is {Solution().majorityElement([2,2,1,1,1,2,2])}')