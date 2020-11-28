class Solution:
    def canPartition(self, nums):
        sums = sum(nums)
        
        if sums % 2 != 0:
            return False
        
        check_sum = sums // 2
        n = len(nums)
        
        dp = [[False for _ in range(check_sum + 1)] for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True
        
        for s in range(1, check_sum + 1):
            dp[0][s] = True if s == nums[0] else False
        
        for i in range(1, n):
            for s in range(1, check_sum + 1):
                included = False
                
                if nums[i] <= s:
                    included = dp[i - 1][s - nums[i]]
                
                notIncluded = dp[i - 1][s]
                
                dp[i][s] = included or notIncluded
        
        return dp[n - 1][check_sum]
                    


def main():
    print(Solution().canPartition([1, 2, 3, 4]))
    print(Solution().canPartition([1, 1, 3, 4, 7]))
    print(Solution().canPartition([2, 3, 4, 6]))

main()