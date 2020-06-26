class Solution:
    def singleNumber(self, nums):
        ones = twos = 0
        
        for num in nums:
            twos = twos | (ones & num)
            
            ones = ones ^ num
            
            common = ~(ones & twos)
            
            
            ones &= common
            twos &= common
            
        return ones


print(f'Solution for [0,1,0,1,0,1,99] is {Solution().singleNumber([0,1,0,1,0,1,99])}')