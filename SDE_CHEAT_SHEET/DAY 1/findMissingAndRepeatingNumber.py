class Solution:

    def findMissingAndRepeating(self,nums, n):
        frequency = {}

        missing, repeating = -1, -1

        for i in range(1, n + 1):
            frequency[i] = 0

        for num in nums:
            frequency[num] += 1

        for num, count in frequency.items():
            if count == 0:
                missing = num
            elif count > 1:
                repeating = num
            
            if repeating != -1 and missing != -1:
                break
        
        return (missing, repeating)

def missingAndRepeating(nums, n):
    i = 0
    missing, repeating = -1, -1

    while i < n:
        num = nums[i]
        correct_location = num - 1

        if num != nums[correct_location]:
            num[i], num[correct_location] = nums[correct_location], num[i]
        else:
            if i != correct_location:
                repeating = num
            
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing = i + 1
            break
    
    return missing, repeating

def missingAndRepeating2(nums, n):
    missingxrepeating = 0
    for num in nums:
        missingxrepeating ^= num
    
    for i in range(1, n + 1):
        missingxrepeating ^= i

    right_set_bit = 1
    while (missingxrepeating & right_set_bit) == 0:
        right_set_bit = right_set_bit << 1

    n1, n2 = 0, 0
    for num in nums:
        if (right_set_bit & num) != 0:
            n1 ^= num
        else:
            n2 ^= num

    for i in range(1, n + 1):
        if (right_set_bit & i) != 0:
            n1 ^= i
        else:
            n2 ^= i

    repeating = -1
    for num in nums:
        if num == n1 or num == n2:
            repeating = num
            break
    
    missing = n1 if repeating == n2 else n2

    return missing, repeating

def missingAndRepeating3(nums, n):
    repeating = sum(nums) - sum(set(nums))
    missing = abs(int(n * (n + 1) / 2) - sum(nums))

    return abs(missing - repeating), repeating

def missingAndRepeating4(nums, n):
    s = sum(nums)
    sn = n*(n + 1)//2

    s2 = 0
    for num in nums:
        s2 += num * num
    
    s2n = (n * (n + 1) * (2 * n + 2)) // 6

    diff = s - sn
    summation = (s2 - s2n) // diff
        
    missing = (summation - diff) // 2
    repeating = summation - missing
        
    return missing, repeating

def main():
    # First Approach
    output = Solution().findMissingAndRepeating([2,2], 2)
    missing, repeating = output
    print(f'Missing is: {missing} Repeating is: {repeating}')

    # Second approach
    output = missingAndRepeating([2,2], 2)
    missing, repeating = output
    print(f'Missing is: {missing} Repeating is: {repeating}')

    # Third approach
    output = missingAndRepeating2([2,2], 2)
    missing, repeating = output
    print(f'Missing is: {missing} Repeating is: {repeating}')

    # Fouth approach
    output = missingAndRepeating3([2,2], 2)
    missing, repeating = output
    print(f'Missing is: {missing} Repeating is: {repeating}')

    # Fifth approach
    output = missingAndRepeating4([2,2], 2)
    missing, repeating = output
    print(f'Missing is: {missing} Repeating is: {repeating}')

main()