from math import inf


# Time Complexity = O(NlogN)
def longestConsectiveSequence(nums):
    if len(nums) < 2:
        return len(nums)

    nums.sort()

    length, maxLength = 1, -inf
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            length += 1
        elif nums[i] == nums[i - 1]:
            pass
        else:
            maxLength = max(length, maxLength)
            length = 1
    
    maxLength = max(length, maxLength)

    return maxLength


# Time Complexity = O(3N) = O(N)
# Space Complexity = O(numberOfDistinctElements)
def longestConsectiveSequence2(nums):
    hashSet = set(nums)
    length, maxLength = 0, -inf
    for i in range(len(nums)):
        if nums[i] - 1 not in hashSet:
            length = 1
            num = nums[i]
            while num + 1 in hashSet:
                length += 1
                num = num + 1
        
    maxLength = max(length, maxLength)


    return maxLength
    



def main():
    # Method 1
    print(longestConsectiveSequence([100,4,200,1,3,2]))
    print(longestConsectiveSequence([0,3,7,2,5,8,4,6,0,1]))
    print(longestConsectiveSequence([1,2,0,1]))

    # Method 2
    print(longestConsectiveSequence2([100,4,200,1,3,2]))
    print(longestConsectiveSequence2([0,3,7,2,5,8,4,6,0,1]))
    print(longestConsectiveSequence2([1,2,0,1]))

main()
