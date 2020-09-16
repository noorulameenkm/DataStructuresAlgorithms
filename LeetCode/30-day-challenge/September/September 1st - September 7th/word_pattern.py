class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return checkWordPattern(pattern, s.split(' '), {})
    

def checkWordPattern(pattern, s_array, lookup):
    if len(s_array) == 0 and len(pattern) == 0:
        return True
    if (len(s_array) == 0 and len(pattern) != 0) or (len(s_array) != 0 and len(pattern) == 0):
        return False
    
    s_word = s_array[0]
    pat_char = pattern[0]
    values = list(lookup.values())
    if s_word in lookup:
        if lookup[s_word] != pattern[0]:
            return False
    elif pat_char in values:
        return False
        
    lookup[s_word] = pattern[0]
    
    return checkWordPattern(pattern[1:], s_array[1:], lookup)
            
        

print(Solution().wordPattern("abba", "dog cat cat fish"))
            
        
        