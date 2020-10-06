class Solution:
    def findNumbers(self, nums):
        count = 0
        
        for num in nums:
            if isEvenNumberOfDigits(num):
                count += 1
                
        return count
            
            
            
            
def isEvenNumberOfDigits(num):
    digits = 0
    
    while num > 0:
        digits += 1
        num = num // 10
    
    return digits % 2 == 0
        

print(Solution().findNumbers([12,345,2,6,7896]))