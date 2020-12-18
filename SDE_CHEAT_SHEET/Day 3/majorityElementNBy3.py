def majorityElement(nums):
    result = set()
    n_by_three = len(nums) // 3

    for i in range(len(nums)):
        count = 0
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                count += 1
        
        if count > n_by_three:
            result.add(nums[i])
    
    return list(result)


def majorityElement2(nums):
    frequency = {}
    result = set()
    n_by_three = len(nums) // 3

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > n_by_three:
            result.add(num)
    
    return list(result)

def majorityElement3(nums):
    num1, num2 = -1, -1
    count1, count2 = 0, 0
    result, n_by_three = set(), len(nums) // 3

    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
        elif count1 == 0:
            num1 = num
            count1 = 1
        elif count2 == 0:
            num2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    

    count1, count2 = 0, 0

    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
    
    if count1 > n_by_three:
        result.add(num1)
    
    if count2 > n_by_three:
        result.add(num2)

    return list(result)



def main():
    # First Approach
    print(majorityElement([3,2,3]))
    print(majorityElement([1]))
    print(majorityElement([1, 2]))
    print(majorityElement([2,2,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9]))

    # Second Approach
    print(majorityElement2([3,2,3]))
    print(majorityElement2([1]))
    print(majorityElement2([1, 2]))
    print(majorityElement2([2,2,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9]))

    # Third Approach
    print(majorityElement3([3,2,3]))
    print(majorityElement3([1]))
    print(majorityElement3([1, 2]))
    print(majorityElement3([2,2,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9]))




main()

        

