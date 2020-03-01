import math

def insert(array, n):
    temp = array[n]
    i = n
    while i > 1 and temp > array[math.floor(i/2)]:
        array[i] = array[math.floor(i/2)]
        i = math.floor(i / 2)
    
    array[i] = temp

def createHeapFromArray(array):
    # Make the zero'th position None
    array.insert(0, None)
    for i in range(2, len(array)):
        insert(array, i)
    


if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    createHeapFromArray(array)
    print(array)
    max_values = array[1:4]
    max_values.sort(reverse = True)
    print(max_values)


        
        