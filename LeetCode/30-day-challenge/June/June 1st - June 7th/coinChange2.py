class Solution:
    def change(self, amount, coins):
        arr = [0 for i in range(amount + 1)]
        arr[0] = 1
        
        for coin in coins:
            for num in range(coin, amount+1):
                arr[num] += arr[num - coin]
        
        return arr[amount]
        



print(f'Solution for amount = 5, coins = [1, 2, 5] is {Solution().change(5, [1, 2, 5])}')