def inversionCount(nums):
    length = len(nums)
    count = 0
    for i in range(length - 1):
        for j in range(length):
            if nums[i] > nums[j]:
                count += 1
    
    return count


def merge(nums, temp, start, start2, end):
    inversion_count = 0
    i, j, k = start, start2, start

    while i < start2 and j <= end:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            inversion_count += (start2 - i)
            j += 1
        
        k += 1

    
    while i < start2:
        temp[k] = nums[i]
        i += 1
        k += 1
    
    while j <= end:
        temp[k] = nums[j]
        j += 1
        k += 1
    

    for i in range(start, end + 1):
        nums[i] = temp[i]
    

    return inversion_count


def mergeSort(nums, temp, left, right):
    inversion_count = 0

    if left < right:
        mid = left + (right - left) // 2

        inversion_count += mergeSort(nums, temp, left, mid)
        inversion_count += mergeSort(nums, temp, mid + 1, right)

        inversion_count += merge(nums, temp, left, mid + 1, right)

    
    return inversion_count

def inversionCount2(nums):
    temp = [0 for i in range(len(nums))]
    return mergeSort(nums, temp, 0, len(nums) - 1)






def main():
    # First Approach
    print(inversionCount([8, 4, 2, 1]))

    # Second Approach
    print(inversionCount2([8, 4, 2, 1]))

main()