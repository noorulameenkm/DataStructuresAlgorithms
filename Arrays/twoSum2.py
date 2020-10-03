def pair_with_targetsum(arr, target_sum):
  result = []
  start, end = 0, len(arr) - 1
  while start < end:
    sum_ = arr[start] + arr[end]
    # sum == target
    if sum_ == target_sum:
      result.append(start)
      result.append(end)
      break
    # sum > target
    elif sum_ > target_sum:
      end -= 1
    else:
      start += 1

  return result


def two_sum_pair(arr, target_sum):
    nums = {}

    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[num] = i
    
    return [-1, -1]


print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))
print(two_sum_pair([1, 2, 3, 4, 6], 6))
print(two_sum_pair([2, 5, 9, 11], 11))