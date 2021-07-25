
"""
    Problem Link:- https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
"""



class Solution:
    def findIntegers(self, n):
        fibo = [0 for _ in range(31)]
        fibo[0] = 1
        fibo[1] = 2
        for i in range(2, 31):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
        
        ans, k, pre_bit = 0, 30, 0
        while k >= 0:
            if (n & (1 << k)):
                ans += fibo[k]
                if pre_bit:
                    return ans
                
                pre_bit = 1
            else:
                pre_bit = 0
            
            k -= 1
        
        return ans + 1
            



print(Solution().findIntegers(n = 5))
print(Solution().findIntegers(n = 1))
print(Solution().findIntegers(n = 2))
            
            
            
        