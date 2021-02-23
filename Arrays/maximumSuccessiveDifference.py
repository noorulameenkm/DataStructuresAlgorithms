from math import inf


def maximumDifference(arr):
    n = len(arr)

    if n < 2:
        return 0

    arr.sort()
    max_ = arr[1] - arr[0]

    for i in range(2, n):
        localDiff = arr[i] - arr[i - 1]
        if localDiff > max_:
            max_ = localDiff
    
    return max_



def maximumDifference2(arr):
    n = len(arr)
    if n < 2:
        return 0
    
    maxVal, minVal = arr[0], arr[0]
    for i in range(1, n):
        maxVal = max(maxVal, arr[i])
        minVal = min(minVal, arr[i])


    maxBuckets = [-inf] * (n - 1)
    minBuckets = [inf] * (n - 1)

    # expected bucket difference
    delta = (maxVal - minVal) // (n - 1)

    for i in range(n):
        if arr[i] == maxVal or arr[i] == minVal:
            continue
            
        index = (arr[i] - minVal) // delta

        if maxBuckets[index] == -inf:
            maxBuckets[index] = arr[i]
        else:
            maxBuckets[index] = max(maxBuckets[index], arr[i])

        
        if minBuckets[index] == inf:
            minBuckets[index] = arr[i]
        else:
            minBuckets[index] = min(arr[i], minBuckets[index])

    
    prevVal, maxGap = minVal, 0

    for i in range(0, n - 1):
        if minBuckets[i] == inf:
            continue
            
        maxGap = max(maxGap, minBuckets[i] - prevVal)
        prevVal = maxBuckets[i]
    
    maxGap = max(maxGap, maxVal - prevVal)

    return maxGap


def main():
    # Approach_1
    print(maximumDifference([1, 5, 10]))

    # Approach_2
    print(maximumDifference2([1, 5, 10]))



main()
