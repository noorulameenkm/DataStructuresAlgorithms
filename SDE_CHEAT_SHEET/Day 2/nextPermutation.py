from itertools import permutations



# Algorithm
# 1. trverse from the second last element and find the index which satisfies value at that index greater than the value at next index -> index1
# 2. traverse from the last element and find the index which has the value which is greater than the index1 value -> index2
# 3. if index1 is there, then swap index1 and index2
# 4. reverse the values from index1 + 1 to the end of the list
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            pass
        elif len(nums) == 2:
            nums[0::] = nums[::-1]
        else:
            length = len(nums)
        
            i = length - 2
        
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1

            if i >= 0:
                j = length - 1
                while j > i and nums[j] <= nums[i]:
                    j -= 1

                nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1:] = nums[i + 1:][::-1]
        
            

def nextPermutation(nums):
    num_permutations = list(permutations(nums))
    
    for i in range(len(num_permutations)):
        if list(num_permutations[i]) == nums:
            break
    
    next_ = list(num_permutations[0]) if i == len(num_permutations) - 1 else list(num_permutations[i + 1])
    nums[0:] = next_[0:]



def main():

    # first Approach
    nums = [1,2,3]
    nextPermutation(nums)
    print(f'Next Permutation of [1, 2, 3] is {nums}')
    nums = [1,2,3,4]
    nextPermutation(nums)
    print(f'Next Permutation of [1, 2, 3, 4] is {nums}')


    # Second Approach
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    print(f'Next Permutation of [1, 2, 3] is {nums}')
    nums = [1,2,3,4]
    Solution().nextPermutation(nums)
    print(f'Next Permutation of [1, 2, 3, 4] is {nums}')
    nums = [1, 2, 4, 3]
    Solution().nextPermutation(nums)
    print(f'Next Permutation of [1, 2, 4, 3] is {nums}')

main()