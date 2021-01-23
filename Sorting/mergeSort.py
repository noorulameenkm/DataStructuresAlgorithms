def merge(nums, start, mid, end):
    tempArr = [0] * len(nums)

    start1, start2 = start, mid + 1
    k = start
    while start1 <= mid and start2 <= end:
        if nums[start1] <= nums[start2]:
            tempArr[k] = nums[start1]
            start1 += 1
        else:
            tempArr[k] = nums[start2]
            start2 += 1
        
        k += 1
    
    while start1 <= mid:
        tempArr[k] = nums[start1]
        k += 1
        start1 += 1
    
    while start2 <= end:
        tempArr[k] = nums[start2]
        k += 1
        start2 += 1

    for s in range(start, end + 1):
        nums[s] = tempArr[s]
    


"""
Time Complexity - O(nlogn)
"""
def mergeSort(nums, start, end):
    if start < end:
        mid = start + (end - start) // 2
        mergeSort(nums, start, mid)
        mergeSort(nums, mid + 1, end)

        merge(nums, start, mid, end)


"""
Time Complexity - O(nlogn)
"""
def mergeSort2(lst):
    """
    Merge sort function
    :param lst: lst of unsorted integers
    """
    if len(lst) > 1:
        mid = len(lst) // 2  # Mid of the list
        left = lst[:mid]  # Dividing the list elements into 2 halves
        right = lst[mid:]

        mergeSort2(left)  # Sorting the first half
        mergeSort2(right)  # Sorting the second half

        # Initializing index variables
        i = 0
        j = 0
        k = 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was right
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1




def main():
    # First Approach
    nums = [17, 25, 31, 13, 2]
    mergeSort(nums, 0, len(nums) - 1)
    print(nums)
    nums = [12, 11, 13, 5, 6]
    mergeSort(nums, 0, len(nums) - 1)
    print(nums)

    # Second Approach
    nums = [17, 25, 31, 13, 2]
    mergeSort2(nums)
    print(nums)
    nums = [12, 11, 13, 5, 6]
    mergeSort2(nums)
    print(nums)


main()