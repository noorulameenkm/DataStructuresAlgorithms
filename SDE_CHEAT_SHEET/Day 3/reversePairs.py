"""
Time Complexity - O(nlogn + n + n)
Space Complexity - O(n)
"""
def merge(nums, temp, start1, start2, end):
    count = 0
    j = start2
    i = start1
    while i < start2:
        while j <= end and nums[i] > (2 * nums[j]):
            j += 1
        
        i += 1
        count += (j - start2)


    i, j, k = start1, start2, start1
    while i < start2 and j <= end:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1

        k += 1
    
    while i < start2:
        temp[k] = nums[i]
        k += 1
        i += 1
    
    while j <= end:
        temp[k] = nums[j]
        j += 1
        k += 1

    k = start1
    while k <= end:
        nums[k] = temp[k]
        k += 1

    return count


def mergeSort(nums, temp, start, end):
    reversePairs = 0
    if start < end:
        mid = start + (end - start) // 2
        reversePairs += mergeSort(nums, temp, start, mid)
        reversePairs += mergeSort(nums, temp, mid + 1, end)
        reversePairs += merge(nums, temp, start, mid + 1, end) 
    return reversePairs


def findReversePairs(nums):
    temp = [0 for i in range(len(nums))]
    return mergeSort(nums, temp, 0, len(nums) - 1)

def findReversePairs2(nums):
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > (2 * nums[j]):
                count += 1
    
    return count

def main():
    # Method 1
    print(findReversePairs([1,3,2,3,1]))
    print(findReversePairs([2,4,3,5,1]))

    # Method 2
    print(findReversePairs2([1,3,2,3,1]))
    print(findReversePairs2([2,4,3,5,1]))


main()