class Solution:
    def search(self, arr, target):
        start, end = 0, len(arr) - 1
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            if arr[mid] == target:
                return True
            elif arr[start] == arr[mid] and arr[mid] == arr[end]:
                start += 1
                end -= 1
            elif arr[start] <= arr[mid]:
                if target >= arr[start] and target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > arr[mid] and target <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False

def pivoted_binary_search(lst, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """

    pivot = find_pivot_point(lst, 0, n - 1)

    # If the list is not rotated
    if pivot == -1:
        return binary_search(lst, 0, n - 1, key)

    # If the list is rotated then find the elements in left sided and right sided list
    if lst[pivot] == key:
        return pivot

    if lst[0] <= key:
        return binary_search(lst, 0, pivot - 1, key)

    return binary_search(lst, pivot + 1, n - 1, key)


def find_pivot_point(lst, low, high):
    """
    Function to pivot in the list
    :param lst: A list of integers
    :param low: Lowest index of the list
    :param high: Highest index of the list
    """

    # base cases
    if high < low:
        return -1

    if high == low:
        return low

    mid = (low + high) // 2

    if mid < high and lst[mid] > lst[mid + 1]:
        return mid

    if mid > low and lst[mid] < lst[mid - 1]:
        return mid - 1

    if lst[low] >= lst[mid]:
        return find_pivot_point(lst, low, mid - 1)

    return find_pivot_point(lst, mid + 1, high)


def binary_search(lst, low, high, key):
    """
    Binary Search function
    :param lst: A list of integers
    :param low: Lowest index of the list
    :param high: Highest index of the list
    :param key: A key to be searched in the list
    """

    if high < low:
        return -1

    mid = (low + high) // 2

    if key == lst[mid]:
        return mid

    if key > lst[mid]:
        return binary_search(lst, (mid + 1), high, key)

    return binary_search(lst, low, (mid - 1), key)



def main():
    print(Solution().search([2,5,6,0,0,1,2], 0))
    print(Solution().search([2,5,6,0,0,1,2], 3))
    lst = [6, 7, 8, 9, 10, 0, 1, 2, 3]
    key = 0

    print("Index of the element is : ",
          pivoted_binary_search(lst, len(lst), key))


main()