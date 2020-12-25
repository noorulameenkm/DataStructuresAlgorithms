import math

def isTripletSequenceExists(nums):
    if len(nums) <= 2:
        return False

    i = 0
    while i < len(nums) - 2:
        j = i + 1

        while j < len(nums) - 1:
            if nums[j] <= nums[i]:
                j += 1
                continue
        
            k = j + 1
            while k < len(nums):
                if nums[k] > nums[j]:
                    return True
                
                k += 1

            j += 1        
        i += 1
    
    return False


def isTripletSequenceExists2(nums):
    if len(nums) < 3:
        return False
    
    numOne, numTwo = math.inf, math.inf

    for num in nums:
        if num < numOne:
            numOne = num
        
        if num > numOne:
            numTwo = min(num, numTwo)
        
        if num > numTwo:
            return True

    return False




def main():
    # First Approach
    print(isTripletSequenceExists([1,2,3,4,5]))
    print(isTripletSequenceExists([5,4,3,2,1]))
    print(isTripletSequenceExists([2,1,5,0,4,6]))
    print(isTripletSequenceExists([5,1,5,5,2,5,4]))
    print(isTripletSequenceExists([1,1,-2,6]))

    # Second Approach
    print(isTripletSequenceExists2([1,2,3,4,5]))
    print(isTripletSequenceExists2([5,4,3,2,1]))
    print(isTripletSequenceExists2([2,1,5,0,4,6]))
    print(isTripletSequenceExists2([5,1,5,5,2,5,4]))
    print(isTripletSequenceExists2([1,1,-2,6]))

main()
