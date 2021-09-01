"""
    Problem Link:- https://leetcode.com/problems/array-nesting/
"""


class Solution:
    def arrayNesting(self, nums):
        n = len(nums)
        visited = [False] * n
        ans = 0

        for i in range(n):
            temp = 0
            while not visited[i]:
                visited[i] = True
                temp += 1
                i = nums[i]

            ans = max(ans, temp)

        return ans


print(Solution().arrayNesting(nums=[5, 4, 0, 3, 1, 6, 2]))
print(Solution().arrayNesting(nums=[0, 1, 2]))
