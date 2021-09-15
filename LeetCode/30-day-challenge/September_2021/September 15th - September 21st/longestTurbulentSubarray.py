from typing import List


"""
    Problem Link:- https://leetcode.com/problems/longest-turbulent-subarray/
"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def compare(is_odd, curr, prev):
            if is_odd:
                return curr < prev
            else:
                return curr > prev

        ans = 1
        for flip in [False, True]:
            left = 0
            for right in range(1, len(arr)):
                is_odd = right & 1
                current = arr[right]
                previous = arr[right - 1]
                if flip:
                    is_odd = not is_odd
                if not compare(is_odd, current, previous):
                    left = right

                ans = max(ans, right - left + 1)

        return ans


print(Solution().maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(Solution().maxTurbulenceSize(arr=[4, 8, 12, 16]))
print(Solution().maxTurbulenceSize(arr=[100]))
