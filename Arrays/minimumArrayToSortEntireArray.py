def minimumArrayLengthToSortEntireArray(array):
    n = len(array)
    start = 0
    while start < n - 1:
        if array[start] > array[start + 1]:
            break

        start += 1
    
    if start == n - 1:
        return [-1]
    
    for end in range(n - 1, 0, -1):
        if array[end] < array[end - 1]:
            break

    min_ = min(array[start : end + 1])
    max_ = max(array[start : end + 1])

    if start > 0:
        for i in range(start):
            if array[i] > min_:
                start = i
                break
            
    
    if end < n - 1:
        for j in range(n - 1, end, -1):
            if array[j] < max_:
                end = j
                break
        
    
    return start, end




def main():
    print(minimumArrayLengthToSortEntireArray([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))
    print(minimumArrayLengthToSortEntireArray([0, 1, 15, 25, 6, 7, 30, 40, 50]))
    print(minimumArrayLengthToSortEntireArray([1, 2, 3]))
    print(minimumArrayLengthToSortEntireArray([ 1, 3, 2, 4, 5 ]))

main()