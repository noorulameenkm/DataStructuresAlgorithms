import math

def maximum_sum_subarray(nums):
    length = len(nums)
    maxSum = -math.inf
    for i in range(length - 1):
        for j in range(i, length):
            localSum = 0
            for k in range(i, j + 1):
                localSum += nums[k]
            
            maxSum = max(maxSum, localSum)
    
    return maxSum


def maximum_sum_subarray2(nums):
    length = len(nums)
    maxSum = -math.inf
    for i in range(length - 1):
        localSum = 0
        for j in range(i, length):
            localSum += nums[j]
            maxSum = max(maxSum, localSum)
    
    return maxSum

def maximum_sum_subarray3(nums):
    length = len(nums)
    if length < 0:
        return 0

    localMaxSum = globalMaxSum = nums[0]
    for i in range(1, length):
        localMaxSum = max(nums[i], localMaxSum + nums[i])
        if localMaxSum > globalMaxSum:
            globalMaxSum = localMaxSum
    
    return globalMaxSum

def maximum_sum_subarray4(nums):
    sum_ = 0
    max_ = -math.inf
    for num in nums:
        sum_ += num
        max_ = max(max_, sum_)
        if sum_ < 0:
            sum_ = 0
    
    return max_

def find_max_sum_subarray_5(lst): 
  if (len(lst) < 1): 
    return 0

  curr_max = lst[0]
  global_max = lst[0]
  length_array = len(lst)
  for i in range(1, length_array):
    if curr_max < 0: 
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    if global_max < curr_max:
      global_max = curr_max

  return global_max




def main():
    # first Approach
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_sum_subarray(nums))
    nums = [-1, -2, -3, -4]
    print(maximum_sum_subarray(nums))
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maximum_sum_subarray(nums))

    # second Approach
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_sum_subarray2(nums))
    nums = [-1, -2, -3, -4]
    print(maximum_sum_subarray2(nums))
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maximum_sum_subarray2(nums))

    # third Approach
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_sum_subarray3(nums))
    nums = [-1, -2, -3, -4]
    print(maximum_sum_subarray3(nums))
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maximum_sum_subarray3(nums))

    # Fourth Approach
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_sum_subarray4(nums))
    nums = [-1, -2, -3, -4]
    print(maximum_sum_subarray4(nums))
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maximum_sum_subarray4(nums))

    # Fifth Approach
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(find_max_sum_subarray_5(nums))
    nums = [-1, -2, -3, -4]
    print(find_max_sum_subarray_5(nums))
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(find_max_sum_subarray_5(nums))
    

main()