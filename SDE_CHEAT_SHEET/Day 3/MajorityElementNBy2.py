
def majorityElementNByTwo(array):
    n_by_two = len(array) // 2

    for i in range(len(array)):
        count = 0
        for j in range(i, len(array)):
            if array[j] == array[i]:
                count += 1
        
        if count > n_by_two:
            return array[i]
    

def majorityElementNByTwo2(array):
    n_by_two = len(array) // 2
    frequency = {}

    for num in array:
        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > n_by_two:
            return num



# Moore's Algorithm
def majorityElementNByTwo3(array):
    count, element = 0, 0

    for num in array:
        if count == 0:
            element = num
        
        if element == num:
            count += 1
        else:
            count -= 1
    
    return element

    

    

def main():
    # First Approach
    print(majorityElementNByTwo([3,2,3]))
    print(majorityElementNByTwo([2,2,1,1,1,2,2]))

    # Second Approach
    print(majorityElementNByTwo2([3,2,3]))
    print(majorityElementNByTwo2([2,2,1,1,1,2,2]))

    # Third Approach
    print(majorityElementNByTwo3([3,2,3]))
    print(majorityElementNByTwo3([2,2,1,1,1,2,2]))

main()