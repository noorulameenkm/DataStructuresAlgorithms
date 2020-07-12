class Solution:
    def findAnagrams(self, s, p):
        
        start, frequency, matched = 0, {}, 0
        result = []
        
        for pat in p:
            if pat not in frequency:
                frequency[pat] = 0
            frequency[pat] += 1
            
        for end in range(len(s)):
            char = s[end]
            
            if char in frequency:
                frequency[char] -= 1
                if frequency[char] == 0:
                    matched += 1
                    
            if matched == len(frequency):
                result.append(start)
                
            if end >= len(p) - 1:
                rem_char = s[start]
                start += 1
                
                if rem_char in frequency:
                    if frequency[rem_char] == 0:
                        matched -= 1
                    frequency[rem_char] += 1
                    
                    
        return result


print(f'Find Anagrams in "cbaebabacd" of "abc" is {Solution().findAnagrams("cbaebabacd", "abc")}')
print(f'Find Anagrams in "abab" of "ab" is {Solution().findAnagrams("abab", "ab")}')