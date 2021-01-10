class Solution:
    def longestSubstring(self, s, k):
        frequency = {}
        
        n = len(s)
        
        if n == 0 or k > n:
            return 0
        
        if k <= 1:
            return n
        
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        
        index = 0
        while index < n and frequency[s[index]] >= k:
            index += 1
        
        if index >= n - 1:
            return index
        
        l1 = self.longestSubstring(s[:index], k)
        l2 = self.longestSubstring(s[index + 1:], k)
        
        return max(l1, l2)
            


def main():
    print(Solution().longestSubstring("aaabb", 3))
    print(Solution().longestSubstring("ababbc", 2))

main()