class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in range(len(magazine)):
            if d.get(magazine[i], 0) == 0:
                d[magazine[i]] = 1
            else:
                d[magazine[i]] += 1
        
        for j in range(len(ransomNote)):
            if d.get(ransomNote[j], 0) == 0:
                return False
            else: 
                d[ransomNote[j]] -= 1
                pass
        
        return True
                
        

print(f'canConstruct? {Solution().canConstruct("aa", "ab")}')
print(f'canConstruct? {Solution().canConstruct("aa", "aab")}')