class Solution:
    def maxPower(self, s: str) -> int:
        start, length, maxLength = 0, 0, 0
        
        frequency = {}
        for end in range(len(s)):
            char = s[end]
            frequency[char] = frequency.get(char, 0) + 1
            length += 1
            
            while len(frequency) > 1:
                rem_char = s[start]
                start += 1
                
                frequency[rem_char] -= 1
                length -= 1
                if frequency[rem_char] == 0:
                    del frequency[rem_char]
                
            maxLength = max(maxLength, length)
            
        return maxLength
        

print(Solution().maxPower("leetcode"))
print(Solution().maxPower("abbcccddddeeeeedcba"))