"""
 Time Complexity - O(logN)
 Time Complexity - O(n)
"""

class Solution:
    def numberOfBits(self, n):
        count = 0

        while n > 0:
            count += 1
            n >>= 1

        return count
    
    def numberOfBits2(self, n):
        count = 0
        while (1 << count) <= n:
            count += 1
        
        return count

    def toBinary(self, n):
        stack = []
        while n > 0:
            stack.insert(0, n % 2)
            n >>= 1

        return stack



if __name__ == '__main__':
    print(Solution().numberOfBits(10))
    print(Solution().toBinary(10))
    print(Solution().numberOfBits2(10))

    print(Solution().numberOfBits(100))
    print(Solution().toBinary(100))
    print(Solution().numberOfBits2(100))

    print(Solution().numberOfBits(245))
    print(Solution().toBinary(245))
    print(Solution().numberOfBits2(245))