class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        start, end = 0, len(nums) - 1
        curr = 0
        
        while curr <= end:
            if nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
            else:
                nums[curr], nums[start] = nums[start], nums[curr]
                start += 1
                curr += 1

def sortColors(nums):
    zeroes = ones = twos = 0
    for num in nums:
        if num == 0:
            zeroes += 1
        elif num == 1:
            ones += 1
        else:
            twos += 1

    j = 0

    while j < len(nums):
        if zeroes != 0:
            nums[j] = 0
            zeroes -= 1
        elif ones != 0:
            nums[j] = 1
            ones -= 1
        else:
            nums[j] = 2
            twos -= 1
        
        j += 1
        

def main():
    nums = [2,0,2,1,1,0]
    print('Before: ', nums)
    Solution().sortColors(nums)
    print('After: ', nums)
    nums = [2,0,2,1,1,0]
    print('Before: ', nums)
    sortColors(nums)
    print('After: ', nums)


main()