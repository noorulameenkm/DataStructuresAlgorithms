from bisect import bisect_left as lower_bound


def getSum(BIT, index):
    # Initialize the result
    s = 0

    # Trvaerse ancestors of BITree 
    while index > 0:

        # Add current element of BITree to sum
        s += BIT[index]

        # update index
        index -= (index & -index)
    return s


def updateBIT(BITree, n, index, value):

    # Traverse all ancestors
    while index <= n:

        # Add 'val' to current node of BIT 
        BITree[index] += value  

        # update the index
        index += (index & -index)



def convert(arr, n):

    # create a copy of arr[] in temp and
    # sort the temp array in increasing order
    temp = [0] * n

    for i in range(n):
        temp[i] = arr[i]
    
    temp.sort()

    # Traverse all array elements
    for i in range(n):

        # lower_bound() Returns pointer to the first element
        # greater than or equal to arr[i]
        arr[i] = lower_bound(temp, arr[i]) + 1



def findElements(arr, n):
    # convert arr[] to an array with values
    # from 1 to n and relative order of smaller
    # and greater elements remains same. For example, 
    # {7, -90, 100, 1} is converted to {3, 1, 4, 2}
    convert(arr, n)

    # create a BIT with size equal to maxelement + 1
    BIT = [0] * (n + 1)

    # To store the smaller elements in right side
    # and greater elements on the left side
    smaller_right = [0] * n
    greater_left = [0] * n

    # Traverse all elements from right 
    for i in range(n - 1, -1, -1):

        # Get count of elements smaller than arr[i]
        smaller_right[i] = getSum(BIT, arr[i] - 1)

        # Add current element to BIT
        updateBIT(BIT, n, arr[i], 1)

    # set BIT for second logic
    for i in range(1, n + 1):
        BIT[i] = 0

    for i in range(n):
        
        # Get count of elements greater than arr[i]
        greater_left[i] = i - getSum(BIT, arr[i])

        # Add current element to BIT
        updateBIT(BIT, n, arr[i], 1)
    
    return smaller_right, greater_left
    


def main():
    arr = [12, 1, 2, 3, 0, 11, 4]
    n = len(arr)

    # Function call
    smaller_right, greater_left = findElements(arr, n)
    print(smaller_right, greater_left)

main()