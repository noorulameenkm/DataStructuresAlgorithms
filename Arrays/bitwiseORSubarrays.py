def bitwiseORSubarray(nums):
    hashMap = {}

    if len(nums) == 1:
        return 1

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            bit = 0
            for k in range(i, j + 1):
                bit |= nums[k]
            
            if bit not in hashMap:
                hashMap[bit] = True


    return len(hashMap)

class Solution:
    def bitwiseORSubarray(self, arr):
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)





def main():
    # Method 1
    print(bitwiseORSubarray([0]))
    print(bitwiseORSubarray([1,1,2]))
    print(bitwiseORSubarray([1,2,4]))

    # Method 3
    print(Solution().bitwiseORSubarray([0]))
    print(Solution().bitwiseORSubarray([1,1,2]))
    print(Solution().bitwiseORSubarray([1,2,4]))

main()