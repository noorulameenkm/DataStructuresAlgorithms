def aggressive_cows(stalls, cows):
    n = len(stalls)

    stalls.sort()

    start, end = 1, stalls[n - 1] - stalls[0]
    res = 0
    while start <= end:
        mid  = start + (end - start) // 2

        if is_possible(stalls, cows, mid):
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return res


def is_possible(stalls, cows, min_distance):

    n = len(stalls)
    cordinate = stalls[0]
    count = 1

    for i in range(1, n):
        if (stalls[i] - cordinate) >= min_distance:
            cordinate = stalls[i]
            count += 1
        
        if count == cows:
            return True
    
    return False






print(aggressive_cows([1,2,4,8,9], 3))