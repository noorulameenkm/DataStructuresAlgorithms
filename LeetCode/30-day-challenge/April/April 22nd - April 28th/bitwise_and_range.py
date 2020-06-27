class Solution:
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n -= (n & -n)
            
        return n
        


print(f'Solution is {Solution().rangeBitwiseAnd(5, 7)}')