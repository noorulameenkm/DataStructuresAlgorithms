class Solution:
    def arrangeCoins(self, n):
        count = 0
        i = 1
        while n - i >= 0:
            count += 1
            n = n - i
            i += 1
        
        return count


print(f'Solution for 5 is {Solution().arrangeCoins(5)}')
            
        