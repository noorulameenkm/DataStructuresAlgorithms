import math

def deleteFromHeap(array, n):
    val = array[1]
    array[1] = array[n]
    array[n] = val
    i = 1
    j = 2 * i
    while j < n - 1:
        if array[j + 1] > array[j]:
            j = j + 1
        
        if array[j] > array[i]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i = j 
            j = j * 2
        else:
            break 

    return val
    
        

def heapify(array, n):
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
        heapify(array, i)
    


if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    createHeapFromArray(array)
    print(array)
    # print(deleteFromHeap(array, len(array) - 1))
    # print(array)
    for i in range(len(array) - 1, 1, -1):
        deleteFromHeap(array, i)
    
    print(array)



        
        