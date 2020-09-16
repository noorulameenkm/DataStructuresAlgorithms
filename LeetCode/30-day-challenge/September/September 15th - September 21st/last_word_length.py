class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start = len(s) - 1
        while start >= 0 and s[start] == ' ':
            start -= 1
        return 0 if start < 0 else getLastWordLength(s, start)
    
    
def getLastWordLength(s, start):
    start = start
    length = 0
    while start >= 0 and s[start] != ' ':
        length += 1
        start -= 1
    
    return length


print(Solution().lengthOfLastWord("Hello World "))