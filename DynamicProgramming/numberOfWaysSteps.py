


def no_of_ways(n):
    arr = [0 for i in range(n + 1)]
    arr[0] = arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]


def no_of_ways2(n, m):
    arr = [0 for i in range(n + 1)]
    arr[0] = arr[1] = 1
    for i in range(2, n + 1):
        j = 1






print(no_of_ways(2))
print(no_of_ways(4))
    