def inertionSort(arr):
    for i in range(1, len(arr)):
        k = i
        while k > 0 and arr[k] < arr[k - 1]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1


def insetionSort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    




def main():

    # First Approach
    arr = [17, 25, 31, 13, 2]
    print('Array Before Sorting: ', arr)
    inertionSort(arr)
    print('Array After Sorting: ', arr)
    arr = [12, 11, 13, 5, 6]
    print('Array Before Sorting: ', arr)
    inertionSort(arr)
    print('Array After Sorting: ', arr)

     # Second Approach
    arr = [17, 25, 31, 13, 2]
    print('Array Before Sorting: ', arr)
    insetionSort2(arr)
    print('Array After Sorting: ', arr)
    arr = [12, 11, 13, 5, 6]
    print('Array Before Sorting: ', arr)
    insetionSort2(arr)
    print('Array After Sorting: ', arr)



main()
    