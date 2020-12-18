def stocks_buy_and_sell(prices):
    profit = 0

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = max(profit, prices[j] - prices[i])

    return profit



def stocks_buy_and_sell2(prices):
    profit, buyPrice = 0, prices[0]

    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - buyPrice)
        buyPrice = min(buyPrice, prices[i])
    
    return profit




def main():
    # First Approach
    print(stocks_buy_and_sell([7,1,5,3,6,4]))

    # Second Approach
    print(stocks_buy_and_sell2([7,1,5,3,6,4]))

main()