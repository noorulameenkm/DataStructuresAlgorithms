"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def suggest_two_products(item_prices, amount):
    balance = {}
    for i in range(len(item_prices)):
        if amount - item_prices[i] in balance:
            return [balance[amount - item_prices[i]], i]
        
        balance[item_prices[i]] = i



item_prices = [2, 30, 56, 34, 55, 10, 11, 20, 15, 60, 45, 39, 51]
amount = 61
print(suggest_two_products(item_prices, amount))