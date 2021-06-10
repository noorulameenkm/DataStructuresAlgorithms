from collections import deque

"""
DP - memoization
Time Complexity - O(n * k)
Space complexity - O(n)
"""
class Solution:
    def maxResult(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        
        memory = {}
        
        def dfs(nums, index, k, n, memory):
            
            if index == n - 1:
                return nums[n - 1]
            
            if index in memory:
                return memory[index]
            
            results = []
            for i in range(index + 1, min(index + k + 1, n)):
                results.append(dfs(nums, i, k, n, memory) + nums[index])
            
            memory[index] = max(results)
            return memory[index]
        
        return dfs(nums, 0, k, len(nums), memory)


"""
Normal recursion
"""
def maxResult(nums, k):
    if len(nums) == 1:
        return nums[0]
    
    def dfs(nums, index, k, n):
        
        if index == n - 1:
            return nums[n - 1]
        
        results = []
        for i in range(index + 1, min(index + k + 1, n)):
            results.append(dfs(nums, i, k, n) + nums[index])
        
        return max(results)
    
    return dfs(nums, 0, k, len(nums))


"""
DP - Tabulation
Time Complexity - O(n * k)
space complexity - O(1)
"""
def maxResultTab(nums, k):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[n - 1] = nums[n - 1]

    for i in range(n-2, -1, -1):
        max_ = nums[i] + dp[i + 1]
        for j in range(i + 2, min(i + k + 1, n)):
            max_ = max(max_, nums[i] + dp[j])
        
        dp[i] = max_

    return dp[0]



def maxResultDeque(nums, k):

    n = len(nums)
    queue = deque([])
    queue.append(0)
    for i in range(1, n):
        
        if(queue[0] + k < i):
            queue.popleft()
        
        nums[i] += nums[queue[0]]
        
        while len(queue) > 0 and nums[i] > nums[queue[len(queue) - 1]]:
            queue.pop()
        
        queue.append(i)
    
    return nums[n - 1]


# Testcase for maxResult
print(maxResult(nums = [1,-1,-2,4,-7,3], k = 2))
print(maxResult(nums = [10,-5,-2,4,0,3], k = 3))
print(maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))


# Testcase for memoization
print(Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2))
print(Solution().maxResult(nums = [10,-5,-2,4,0,3], k = 3))
print(Solution().maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))


# Testcase for Tabulation
print(maxResultTab(nums = [1,-1,-2,4,-7,3], k = 2))
print(maxResultTab(nums = [10,-5,-2,4,0,3], k = 3))
print(maxResultTab(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))


# Testcase for deque
print(maxResultDeque(nums = [1,-1,-2,4,-7,3], k = 2))
print(maxResultDeque(nums = [10,-5,-2,4,0,3], k = 3))
print(maxResultDeque(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))