"""
    Problem Link:- https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        s_t = {}
        t_s = {}
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            if s_char in s_t and s_t[s_char] != t_char:
                return False
            
            if t_char in t_s and t_s[t_char] != s_char:
                return False
            
            s_t[s_char] = t_char
            t_s[t_char] = s_char
        
        return True
                
        


print(Solution().isIsomorphic(s = "egg", t = "add"))
print(Solution().isIsomorphic(s = "foo", t = "bar"))
print(Solution().isIsomorphic(s = "paper", t = "title"))