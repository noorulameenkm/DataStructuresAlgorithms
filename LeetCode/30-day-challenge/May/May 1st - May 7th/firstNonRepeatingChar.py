class Solution:
    def firstUniqChar(self, s):
        d = {}
        
        for i in range(len(s)):
            if d.get(s[i], 0) == 0:
                d[s[i]] = [1, i]
            else:
                d[s[i]] = [d[s[i]][0] + 1, i]
        
        for key,val in d.items():
            if val[0] == 1:
                return val[1]
            
        
        return -1
        
        
        

print(f'First None repeating character index is {Solution().firstUniqChar("leetcode")}')