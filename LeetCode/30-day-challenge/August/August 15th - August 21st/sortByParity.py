class Solution:
    def sortArrayByParity(self, A):
        return [x for x in A if x % 2 == 0] + [y for y in A if y % 2 != 0]




print(Solution().sortArrayByParity([3,1,2,4]))
        