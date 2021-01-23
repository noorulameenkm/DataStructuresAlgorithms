"""
Time Complexity - O(n ^ 2)
"""
def bubbleSort(nums):
    n = len(nums)

    for i in range(n):

        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    
    return nums



def main():
    print(bubbleSort([17, 25, 31, 13, 2]))
    print(bubbleSort([12, 11, 13, 5, 6]))
    print(bubbleSort([17, 25, 31, 13, 2]))

main()