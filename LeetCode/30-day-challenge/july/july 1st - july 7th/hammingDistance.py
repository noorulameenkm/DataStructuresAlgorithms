class Solution:
    def hammingDistance(self, x, y):
        _xor = x ^ y
        
        bits = 0
        while _xor > 0:
            bits = bits + (_xor & 1)
            _xor = _xor >> 1
        
        
        return bits


print(f'Solution for x = 5 or y = 4 is {Solution().hammingDistance(5, 4)}')
print(f'Solution for x = 1 or y = 4 is {Solution().hammingDistance(1, 4)}')