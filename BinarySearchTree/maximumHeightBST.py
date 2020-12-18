from bisect import bisect_left

def maximum_height_bst(arr):
    maxHeight = 0

    for i in range(len(arr)):
        root = arr[i]

        leftCount = 0
        rightCount = 0

        for j in range(i):
            if arr[j] < root:
                leftCount += 1
        
        for j in range(i + 1, len(arr)):
            if arr[j] > root:
                rightCount += 1
        
        maxHeight = max(maxHeight, max(leftCount, rightCount))
    
    return maxHeight

def getSum(BIT, index):
    s = 0

    while index > 0:
        s += BIT[index]

        index -= (index & -index)
    
    return s


def updateBIT(BIT, index, n, value):

    while index <= n:

        BIT[index] += value

        index += (index & -index)

def convert(arr):
    temp = [0] * len(arr)
    
    for i in range(len(arr)):
        temp[i] = arr[i]
    
    temp.sort()

    for i in range(len(arr)):
        arr[i] = bisect_left(temp, arr[i]) + 1
    


def maximum_height_bst2(arr):

    # Convert the arr numbers to range from 1 to n
    convert(arr)
    # length
    n = len(arr)

    # initalise the array to store the max of max of left and right
    result = [0] * n

    # initialise BITree
    BIT = [0] * (n + 1)

    for i in range(n):

        result[i] = getSum(BIT, arr[i] - 1)

        updateBIT(BIT, arr[i], n ,1)
    

    for i in range(n + 1):
        BIT[i] = 0 

    for i in range(n - 1, -1, -1):

        curr = n - i - 1
        result[i] = max(result[i], curr - getSum(BIT, arr[i]))

        updateBIT(BIT, arr[i], n ,1)

    
    return max(result)



def main():
    # First Approach
    print(maximum_height_bst([5, 4, 6, 2, 3, 4]))
    print(maximum_height_bst([12, 1, 2, 3, 0, 11, 4]))

    # Second Approach
    print(maximum_height_bst2([5, 4, 6, 2, 3, 4]))
    print(maximum_height_bst2([12, 1, 2, 3, 0, 11, 4]))

main()