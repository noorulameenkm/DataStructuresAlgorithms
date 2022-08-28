"""
    Time Complexity - O(n^2)
    Space Complexity - O(n)
"""
def suggest_three_products(item_prices):
    item_prices.sort()
    res = []
    for i in range(len(item_prices) - 2):
        if item_prices[i] > 200:
            continue

        two_sum(item_prices, item_prices[i], i, res)
    
    return res


def two_sum(item_prices, val, i, res):
    sum_required = 200 - val
    j, k = i + 1, len(item_prices) - 1
    while j < k:
        if item_prices[j] + item_prices[k] == sum_required:
            res.append([val, item_prices[j], item_prices[k]])
            j += 1
            while j < k and item_prices[j] == item_prices[j - 1]:
                j += 1
            
            k =- 1
            while k > j and item_prices[k] == item_prices[k - 1]:
                k =- 1

        elif item_prices[j] + item_prices[k] < sum_required:
            j += 1
        else:
            k -= 1
    

## Driver code
item_prices = [100, 75, 150, 200, 50, 65, 40, 30, 15, 25, 60]
print(suggest_three_products(item_prices))