def numberOfSubArrays(nums, xor):
    count = 0 
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            xorValue = 0
            for k in range(i, j + 1):
                xorValue ^= nums[k]

            if xorValue == xor:
                count += 1
    
    return count



def numberOfSubArrays2(nums, xor):
    xorValue, count = 0, 0
    hashMap = {}
    for i in range(len(nums)):
        xorValue ^= nums[i]

        if xorValue == xor:
            count += 1
        
        y = xorValue ^ xor
        if y in hashMap:
            count += hashMap[y]
        
        hashMap[xorValue] = hashMap.get(xorValue, 0) + 1
    
    return count




def main():
    # Method 1
    print(numberOfSubArrays([4, 2, 2, 6, 4], 6))
    print(numberOfSubArrays([5, 6, 7, 8, 9], 5))
    print(numberOfSubArrays([5, 6, 7, 8, 9, 6], 6))

    # Method 2
    print(numberOfSubArrays2([4, 2, 2, 6, 4], 6))
    print(numberOfSubArrays2([5, 6, 7, 8, 9], 5))
    print(numberOfSubArrays2([5, 6, 7, 8, 9, 6], 6))


main()