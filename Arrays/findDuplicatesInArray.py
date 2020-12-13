# InterviewBit Question
def repeatedNumber(A):
        if len(A) <= 1:
            return -1
        
        slow = A[0]
        fast = A[0]
        
        while True:
            slow = A[slow]
            fast = A[A[fast]]
            
            if slow == fast:
                break
        
        slow = A[0]
        while slow != fast:
            slow = A[slow]
            fast = A[fast]
        
        return slow


def repeatedNumber2(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > 1:
            return num
    
    return -1

def repeatedNumber3(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]

    return -1

def repeatedNumber4(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
        
        i += 1

    return -1

def main():

    # First Approach
    print(repeatedNumber([3, 4, 1, 4, 1]))
    print(repeatedNumber([3]))

    # second Approach
    print(repeatedNumber2([3, 4, 1, 4, 1]))
    print(repeatedNumber2([3]))

    # third Approach
    print(repeatedNumber3([3, 4, 1, 4, 1]))
    print(repeatedNumber3([3]))

    # fourth Approach
    print(repeatedNumber4([3, 4, 1, 4, 1]))
    print(repeatedNumber4([3]))


main()