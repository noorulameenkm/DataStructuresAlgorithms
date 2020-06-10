class Solution:
    def findComplement(self, num):
        temp = num
        bit = 1
        while temp != 0:
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        
        return num


print(f'Solution for 10 is {Solution().findComplement(10)}')
print(f'Solution for 5 is {Solution().findComplement(5)}')