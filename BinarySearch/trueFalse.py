"""
    Time Complexity - O(logN)
    Space Complexity - O(1)
"""

def find_boundary_1(arr):
    n = len(arr)
    start, end = 0, n - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] == True:
            if mid > start and arr[mid - 1] == True:
                end = mid - 1
            else:
                return mid
        else:
            start = mid + 1

    return -1


def find_boundary_2(arr):
    n = len(arr)
    start, end = 0, n - 1
    index = -1
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] == True:
            index = mid
            end = mid - 1 
        else:
            start = mid + 1
    
    return index


if __name__ == '__main__':
    print(find_boundary_1([False, False, True, True, True]))
    print(find_boundary_1([True]))
    print(find_boundary_1([False, False, False]))
    print(find_boundary_1([True, True, True, True, True]))
    print(find_boundary_1([False, True]))

    print(find_boundary_2([False, False, True, True, True]))
    print(find_boundary_2([True]))
    print(find_boundary_2([False, False, False]))
    print(find_boundary_2([True, True, True, True, True]))
    print(find_boundary_2([False, True]))
