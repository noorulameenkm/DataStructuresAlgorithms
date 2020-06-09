class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        n = self.reverseNumber(x)
        return x == n
    
    def reverseNumber(self,x):
        n = 0
        while x != 0:
            n = (n * 10) + (x % 10)
            x = int(x / 10)
        
        return n


print(f'Is palindrome 121 {Solution().isPalindrome(121)}')
print(f'Is palindrome 100 {Solution().isPalindrome(100)}')
        