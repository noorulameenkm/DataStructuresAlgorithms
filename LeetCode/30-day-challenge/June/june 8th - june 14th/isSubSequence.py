class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])

        return self.isSubsequence(s, t[1:])



print(f'Is subsequence {Solution().isSubsequence("axc","ahbgdc")}')
print(f'Is subsequence {Solution().isSubsequence("abc","ahbgdc")}')
        