"""
    Problem Link:- https://leetcode.com/problems/orderly-queue/
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            n = len(s)
            for _ in range(n):
                new_s = s[1:] + s[0]
                ans = min(ans, new_s)
                s = new_s
            return ans
        else:
            return "".join(sorted(s))


print(Solution().orderlyQueue(s="cba", k=1))
print(Solution().orderlyQueue(s="baaca", k=3))
