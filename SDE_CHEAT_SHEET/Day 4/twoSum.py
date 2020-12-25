class Solution:
    def twoSum(self, nums, target):
        s = list(nums)
        nums.sort()
        start, end = 0, len(nums) - 1
        result = [0, 0]
        while start < end:
            if nums[start] + nums[end] == target:
                result = [nums[start], nums[end]]
                break
            elif (nums[start] + nums[end]) < target:
                start += 1
            else:
                end -= 1
        
        k = [-1, -1]
        for i in range(len(s)):
            if s[i] == result[0] or s[i] == result[1]:
                if k[0] == -1:
                    k[0] = i
                else:
                    k[1] = i
                    break

        return k


def twoSum2(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum3(nums, target):
    map_ = {}
    for i in range(len(nums)):
        if (target - nums[i]) in map_:
            return [map_[target - nums[i]], i]
        else:
            map_[nums[i]] = i

        

def main():
    # Method 1
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([3,2,4], 6))

    # Method 2
    print(twoSum2([2,7,11,15], 9))
    print(twoSum2([3,2,4], 6))

    # Method 3
    print(twoSum3([2,7,11,15], 9))
    print(twoSum3([3,2,4], 6))


main()