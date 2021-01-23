
"""
Time Complexity - O(n ^ 2)
"""
def selectionSort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums





def main():
    print(selectionSort([17, 25, 31, 13, 2]))
    print(selectionSort([12, 11, 13, 5, 6]))
    print(selectionSort([17, 25, 31, 13, 2]))

main()