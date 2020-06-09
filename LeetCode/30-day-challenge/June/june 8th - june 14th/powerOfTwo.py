class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        return (n & (n - 1)) == 0


print(f'Solution for 12 is {Solution().isPowerOfTwo(12)}')
print(f'Solution for 16 is {Solution().isPowerOfTwo(16)}')