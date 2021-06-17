from math import inf

def subarrays_with_bounded_maximum(arr, left, right):
    count = 0
    for i in range(len(arr)):
        max_ = -inf
        for j in range(i, len(arr)):
            max_ = max(max_, arr[j])

            if max_ >= left and max_ <= right:
                count += 1
                continue

            if max_ > right:
                break
    
    return count


def numSubarrayBoundedMax(nums, left, right):
        
    start, total = 0, 0
    till_here = 0
    
    for end in range(len(nums)):
        
        if nums[end] >= left and nums[end] <= right:
            till_here = end - start + 1
            total += till_here
        
        if nums[end] < left:
            total += till_here
        
        if nums[end] > right:
            start = end + 1
            till_here = 0
        

    return total

# Test case 1
print(subarrays_with_bounded_maximum([2, 1, 4, 3], 2, 3))

# Test case 2
print(numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))