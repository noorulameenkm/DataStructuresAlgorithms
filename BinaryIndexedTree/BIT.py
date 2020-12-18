# Returns sum of arr[0..index]. This function assumes 
# that the array is preprocessed and partial sums of 
# array elements are stored in BITree[]. 
def getSum(BITree, i):
    # Initialize the result
    sum_ = 0

    # index in BITree is one more than the index in normal array
    i += 1


    while i > 0:

        # Add the current element BITree to sum_
        sum_ += BITree[i]

        # go to the parent
        i -= (i & -i)

    return sum_



# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree.
def updatebit(BITree, n, i, val):

    # index of BITree will be one more than the index of normal array
    i += 1

    # Traverse all the ancestors and add 'val'
    while i <= n:

        # Add val to the current node
        BITree[i] += val
    
        # update index to that of parent in update view
        i += (i & (-i))


def construct(arr, n):
    # Create and initialize BITree[] as 0 
    BITree = [0] * (n + 1)

    # Store the actual values in BITree[] using update() 
    for i in range(0, n):
        updatebit(BITree, n, i, arr[i])
    
    return BITree




def main():
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    BITree = construct(arr, len(arr))
    print(getSum(BITree, 5))
    print(getSum(BITree, 5) - getSum(BITree, 1))


main()

