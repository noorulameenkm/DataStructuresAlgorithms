class Solution:
    def isHappy(self,n):
        reached = 0
        d = {}
        while True:
            n = self.squareOfDigits(n)
            
            if n == 1:
                reached = 1
                break
            else:
                if d.get(n, None) is None:
                    d[n] = True
                else:
                    break
                    
        if reached == 0:
            return False
        
        return True
                  
                
    def squareOfDigits(self, n):
        num = 0
        while n != 0:
            k = n % 10
            num = num + (k * k)
            n = int(n / 10)
        
        return num



print(f'Is 19 a happy number? {Solution().isHappy(19)}')