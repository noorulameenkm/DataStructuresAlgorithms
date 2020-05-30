class Solution:
    def isHappy(self,n):
        slow = n
        fast = n
        while True:
            slow = self.squareOfDigits(slow)
            fast = self.squareOfDigits(self.squareOfDigits(fast))
            
            if slow != fast:
                continue
            else:
                break
                    
        return (slow == 1)
                  
                
    def squareOfDigits(self, n):
        num = 0
        while n != 0:
            k = n % 10
            num = num + (k * k)
            n = int(n / 10)
        
        return num



print(f'Is 19 a happy number? {Solution().isHappy(19)}')