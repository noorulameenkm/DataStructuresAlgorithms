import math

class Solution:
    def numTrees(self, n):
        return int(math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))





print(f'Solution for 4 nodes {Solution().numTrees(4)}')
print(f'Solution for 5 nodes {Solution().numTrees(5)}')