class Solution:
    def findDuplicate(self, nums):
        i, length = 0, len(nums)
        
        while i < length:
            num = nums[i]
            correct_location = nums[i] - 1
            
            if num != nums[correct_location]:
                nums[i], nums[correct_location] = nums[correct_location], nums[i]
            else:
                if i != correct_location:
                    return nums[i]
                
                i += 1


def find_duplicate_number(nums):
    slow, fast = nums[0], nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]

    return slow
    


def main():
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(find_duplicate_number([1,3,4,2,2]))
    print(Solution().findDuplicate([3,1,3,4,2]))
    print(find_duplicate_number([3,1,3,4,2]))

main()