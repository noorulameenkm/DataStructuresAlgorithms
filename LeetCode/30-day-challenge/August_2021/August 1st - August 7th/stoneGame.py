from functools import lru_cache

"""
    Problem Link:- https://leetcode.com/problems/stone-game/
    Learn Minimax Game Theory
"""


class Solution:
    def stoneGame(self, piles):

        @lru_cache(None)
        def dp(left, right):
            if left > right:
                return 0

            if (right - left) & 1:
                return max(piles[left] + dp(left + 1, right), dp(left, right - 1) + piles[right])
            else:
                return min(-piles[left] + dp(left + 1, right), dp(left, right - 1) - piles[right])
        return dp(0, len(piles) - 1) > 0


print(Solution().stoneGame(piles=[5, 3, 4, 5]))
