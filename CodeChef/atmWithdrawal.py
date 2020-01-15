# cook your dish here

try:
    if __name__ == '__main__':
        amount, balance = [i for i in input().split(' ')]
        amount = int(amount)
        balance = float(balance)
        if amount + 0.5 <= balance and amount % 5 == 0:
            balance = balance - (amount + 0.5)
        
        
        print("%.2f" % balance)

except Exception as e:
    pass
        