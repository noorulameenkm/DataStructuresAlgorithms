class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start, frequency, matched = 0, {}, 0
        
        for s in s1:
            if s not in frequency:
                frequency[s] = 0
            frequency[s] += 1
            
        for end in range(len(s2)):
            
            char = s2[end]
            
            if char in frequency:
                frequency[char] -= 1
                if frequency[char] == 0:
                    matched += 1
                    
            if matched == len(frequency):
                return True
            
            if end >= len(s1) - 1:
                rem_char = s2[start]
                
                start += 1
                
                if rem_char in frequency:
                    if frequency[rem_char] == 0:
                        matched -= 1
                    frequency[rem_char] += 1
                    
        return False
                




print(f'Solution of "ab" and "eidbaooo" is {Solution().checkInclusion("ab", "eidbaooo")}')
print(f'Solution of "ab" and "eidboaoo" is {Solution().checkInclusion("ab", "eidboaoo")}')