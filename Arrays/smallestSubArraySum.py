import math

class Solution:
    def smallestSubArray(self, s, arr):
        start, minLength = 0, math.inf
        sum_= 0
        for end in range(len(arr)):
            sum_ += arr[end]

            while sum_ >= s:
                index = end - start + 1
                if index < minLength:
                    minLength = index
                sum_ -= arr[start]
                start += 1
            
        
        return minLength if minLength != math.inf else 0




print(f'Minimum length subarray sum of [2, 1, 5, 2, 8] and 7 is {Solution().smallestSubArray(7, [2, 1, 5, 2, 8])}')
print(f'Minimum length subarray sum of [3, 4, 1, 1, 6] and 8 is {Solution().smallestSubArray(8, [3, 4, 1, 1, 6])}')


