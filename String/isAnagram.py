class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        
        for s_ in s:
            freq[s_] = freq.get(s_, 0) + 1
        
        for t_ in t:
            if t_ not in freq:
                return False
            else:
                freq[t_] -= 1
                if freq[t_] == 0:
                    del freq[t_]
                    
        if len(freq) == 0:
            return True
        
        return False
        


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))