class Solution:
    def numJewelsInStones(self, J, S):
        totalJewels = 0
        for i in range(len(S)):
            totalJewels = totalJewels + 1 if S[i] in J else totalJewels
        return totalJewels
        




print(f'totalNUmber Of jewels is {Solution().numJewelsInStones("aA", "aAAbbbb")}')