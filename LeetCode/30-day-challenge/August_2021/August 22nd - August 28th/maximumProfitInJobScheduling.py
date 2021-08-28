"""
    Problem Link:- https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""


class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit))
        start_times = [job[0] for job in jobs]
        n = len(start_times)
        cache = {}

        def binary_search(target):
            low, high = 0, n - 1
            res = -1
            while low <= high:

                mid = low + (high - low) // 2
                if start_times[mid] >= target:
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return res

        def dp(i):
            if i >= n:
                return 0

            key = f'{i}'
            if key in cache:
                return cache[key]

            next_index = binary_search(jobs[i][1])
            profit = max(dp(i + 1), jobs[i][2] + dp(n if next_index == -1 else next_index))
            cache[key] = profit
            return cache[key]

        return dp(0)


print(Solution().jobScheduling(
    startTime=[1, 2, 3, 3],
    endTime=[3, 4, 5, 6],
    profit=[50, 10, 40, 70]))
print(Solution().jobScheduling(
    startTime=[1, 2, 3, 4, 6],
    endTime=[3, 5, 10, 6, 9],
    profit=[20, 20, 100, 70, 60]))
print(Solution().jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
