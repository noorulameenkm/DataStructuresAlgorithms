import random

def choose_pivot(left, right):

    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    return max(min(i1, i2), min(max(i1, i2), i3))

def partition(nums, left, right):
    pivot_index = choose_pivot(left, right) #index of pivot

    nums[right], nums[pivot_index] = nums[pivot_index], nums[right] # put the pivot at the end

    pivot = nums[right] # Pivot
    i = left - 1  # All the elements less than or equal to the
    # pivot go before or at 

    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1], nums[right] = nums[right], nums[i + 1]

    return i + 1


"""
  Time Complexity - O(nlogn)
"""
def quickSort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)

        quickSort(nums, left, pivot - 1)
        quickSort(nums, pivot + 1, right)


def main():
    # First Approach
    nums = [17, 25, 31, 13, 2]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)
    nums = [12, 11, 13, 5, 6]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)

main()


