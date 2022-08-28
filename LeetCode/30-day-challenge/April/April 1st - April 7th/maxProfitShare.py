from math import inf
class Solution:
    def maxProfit(self, prices):
        profit = 0
        
        n = len(prices)
        i = 0
        while i < (n - 1):
            buy = sell = None
            
            while (i < (n - 1)) and (prices[i + 1] < prices[i]):
                i += 1
            
            if i == n-1:
                break
            
            buy = i
            
            i = i + 1
            
            while (i < (n - 1)) and (prices[i + 1] > prices[i]):
                i += 1
                
                
            sell = i
            
            if buy is not None and sell is not None:
                profit = profit + (prices[sell] - prices[buy])
                buy = sell = None
            
            i = i + 1
            
            
        return profit
        

def maxProfit(prices):
    min_ = inf
    profit = -inf
    for price in prices:
        min_ = min(min_, price)

        if price - min_ > profit:
            profit = price - min_

    return profit

            
print(f'The Max Profit is {Solution().maxProfit([7,1,5,3,6,4])}')   
print(f'The Max Profit is {maxProfit([7,1,5,3,6,4])}')
        