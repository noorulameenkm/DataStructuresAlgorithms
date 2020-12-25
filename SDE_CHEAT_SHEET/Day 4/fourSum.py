def fourSum(nums, target):
    result = []
    nums.sort()
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
        
            findQuadraplets(nums, i, j, target, result)

    return result


def findQuadraplets(nums, i, j, target, result):
    left, right = j + 1, len(nums) - 1
    curr_target = target - (nums[i] + nums[j])
    while left < right:
        if (nums[left] + nums[right]) == curr_target:
            result.append([nums[i], nums[j], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif (nums[left] + nums[right]) < curr_target:
            left += 1
        else:
            right -= 1


def fourSum2(nums, target):
    result = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            for k in range(j + 1, len(nums) - 1):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                    
                for l in range(k + 1, len(nums)):
                    if l > k + 1 and nums[l] == nums[l - 1]:
                        continue

                    if (nums[i] + nums[j] + nums[k] + nums[l]) == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])


    return result
                    


def main():
    # Method 1
    print(fourSum([1,0,-1,0,-2,2], 0))
    print(fourSum([], 0))

    # Method 2
    print(fourSum2([1,0,-1,0,-2,2], 0))
    print(fourSum2([], 0))


main()