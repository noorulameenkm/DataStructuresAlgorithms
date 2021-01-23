class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxOnes, length = -1, 0
        
        for end in range(len(nums)):
            
            if nums[end] == 1:
                length += 1
            
            if end == len(nums) - 1 or nums[end] == 0:
                maxOnes = max(maxOnes, length)
                length = 0
                
                
        return maxOnes


def findMaxConsecutiveOnes2(nums):
    count, maxCount = 0, 0
    for num in nums:
        if num == 0:
            count = 0
            continue

        if num == 1:
            count += 1
            maxCount = max(maxCount, count)
            continue

    return maxCount



def main():
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print(findMaxConsecutiveOnes2([1,1,0,1,1,1]))


main()