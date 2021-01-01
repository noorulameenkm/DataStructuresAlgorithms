def powXNModP(x, n, p):
    res = 1

    x = x % p

    if x == 0:
        return 0
    
    while n > 0:

        if n % 2 == 0:
            n = n / 2
            x = (x * x) % p
        else:
            n = n - 1
            res = (res * x) % p
        
    return res




def main():
    print(powXNModP(2, 3, 3))
    print(powXNModP(2, 3, 5))
    print(powXNModP(2, 5, 13))

main()