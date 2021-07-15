"""
    https://leetcode.com/problems/valid-triangle-number/
"""

def triangleNumber(nums):
        def binary_search(start, end):
            index = -1
            while start <= end:
                mid = start + (end - start) // 2
                if target > nums[mid]:
                    index = mid
                    start = mid + 1
                else:
                    end = mid - 1
            return index
        
            
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        nums.sort()
        for first in range(n - 2):
            for second in range(first + 1, n - 1):
                target = nums[first] + nums[second]
                index = binary_search(second + 1, n - 1)
                if index > -1:
                    count += (index - second)
        
        return count


def triangleNumber2(nums):
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        nums.sort()
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
                
                
        return count

# first Approach
print(triangleNumber(nums = [2,2,3,4]))
print(triangleNumber(nums = [4,2,3,4]))


# Second Approach
print(triangleNumber2(nums = [2,2,3,4]))
print(triangleNumber2(nums = [4,2,3,4]))