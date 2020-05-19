class Solution:
    def singleNumber(self, nums):
        d = {}
        for num in nums:
            if d.get(num, -1) is -1:
                d[num] = 1
            else:
                d[num] = d[num] + 1
                
        
        unique = -1
        
        for key,val in d.items():
            if val == 1:
                unique = key
                break
        
        return unique

soln = Solution()
print(soln.singleNumber([1,2,1,3,2,4,5,5,4]))