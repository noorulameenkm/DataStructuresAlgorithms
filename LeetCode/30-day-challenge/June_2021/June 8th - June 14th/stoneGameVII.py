from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        sum_ = 0
        
        for s in stones:
            sum_ += s
        
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        return solve(0, n - 1, sum_, stones, dp)
    

def solve(left, right, sum_, stones, dp):
    if left == right:
        return 0
    
    if right - left == 1:
        return max(stones[left], stones[right])
    
    if dp[left][right] != -1:
        return dp[left][right]

    diff = max(sum_ - stones[left] - solve(left + 1, right, sum_ - stones[left], stones, dp),
              sum_ - stones[right] - solve(left, right - 1, sum_ - stones[right], stones, dp))
    
    dp[left][right] = diff
    
    return dp[left][right]




# Test1
print(Solution().stoneGameVII(stones = [5,3,1,4,2]))
print(Solution().stoneGameVII(stones = [7,90,5,1,100,10,10,2]))
        