class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        
        frequency = {}
        
        start, maxLength, length = 0, -1, 0
        
        for end in range(len(s)):
            char = s[end]
            
            length += 1
            
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
            
            while frequency[char] > 1:
                remChar = s[start]
                start += 1
                
                frequency[remChar] -= 1
                length -= 1
                
                if frequency[remChar] == 0:
                    del frequency[remChar]
            
            maxLength = max(maxLength, length)
                
        return maxLength


print(Solution().lengthOfLongestSubstring("abcabcbb"))
            
            
        