def searchInMatrix(matrix, val):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == val:
                return True

    return False



def searchInMatrix2(matrix, val):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    n, m = len(matrix), len(matrix[0])

    index = -1
    for i in range(n):
        if val >= matrix[i][0] and val <= matrix[i][m - 1]:
            index = i
            break
            
        i += 1

    if index == -1:
        return False

    
    return BinarySearch(matrix[index], val)


def BinarySearch(array, val):
    start, end = 0, len(array)

    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] == val:
            return True
        elif val < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return False

def searchInMatrix3(matrix, val):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    
    n, m = len(matrix), len(matrix[0])
    start, end = 0, (n * m) - 1

    while start <= end:
        mid = start + (end - start) // 2 

        midIndex_i = mid // m
        midIndex_j = mid % m

        if matrix[midIndex_i][midIndex_j] == val:
            return True
        elif val < matrix[midIndex_i][midIndex_j]:
            end = mid - 1
        else:
            start = mid + 1
    
    return False







def main():
    # First Approach
    print(searchInMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print(searchInMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))

    # Second Approach
    print(searchInMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print(searchInMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))

    # Third Approach
    print(searchInMatrix3([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print(searchInMatrix3([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))

main()