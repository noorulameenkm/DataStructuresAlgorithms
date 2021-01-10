def largestSubArrayZero1(nums):
    maxLength, n = 0, len(nums)
    for i in range(n):
        for j in range(i, n):
            sum_ = 0
            for k in range(i, j + 1):
                sum_ += nums[k]

            if sum_ == 0:
                maxLength = max(maxLength, j - i + 1)

    return maxLength



def largestSubArrayZero2(arr):
    hashSet = {}
    sum_, maxLength = 0, 0
    n = len(arr)
    for i in range(n):
        sum_ += arr[i]
        if sum_ == 0:
            maxLength = max(maxLength, i + 1)
        else:
            if sum_ in hashSet:
                index = hashSet[sum_]
                maxLength = max(maxLength, i - index)
            else:
                hashSet[sum_] = i
    
    return maxLength




def main():
    # Method 1
    print(largestSubArrayZero1([15,-2,2,-8,1,7,10,23]))

    # Method 2
    print(largestSubArrayZero2([15,-2,2,-8,1,7,10,23]))


main()
