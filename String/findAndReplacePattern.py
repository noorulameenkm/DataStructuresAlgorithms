"""
N - number of words
k - length of the pattern
Time Complexity - O(N * K)
Space Complexity - O(N * K)
"""
class Solution:
    def findAndReplacePattern(self, words, pattern):
        results = []
        for word in words:
            if isMatch(word, pattern) is True:
                results.append(word)
        
        return results
        
        
def isMatch(string, pattern):
    patternToWord, wordToPattern = {}, {}
    if len(string) != len(pattern):
        return False
    
    n = len(string)
    for i in range(n):
        pat, char = pattern[i], string[i]
        if pat in patternToWord and patternToWord[pat] != char:
            return False
        
        if char in wordToPattern and wordToPattern[char] != pat:
            return False
        
        if pat not in patternToWord:
            patternToWord[pat] = char
        
        if char not in wordToPattern:
            wordToPattern[char] = pat
    
    return True



print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
print(Solution().findAndReplacePattern(words = ["a","b","c"], pattern = "a"))