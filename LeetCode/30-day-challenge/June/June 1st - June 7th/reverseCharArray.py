class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1


s = ['h', 'e', 'l', 'l', 'o']
Solution().reverseString(s)
print(f'Reversed array is {s}')
        
        