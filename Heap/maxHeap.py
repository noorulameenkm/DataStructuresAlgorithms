from math import floor


def max_heapify(heap, index, length):

    left = 2 * index
    right = 2 * index + 1
    largest = index

    # Finding the index of the largest element
    if left <= length and heap[left] > heap[largest]:
        largest = left
    if right <= length and heap[right] > heap[largest]:
        largest = right
    
    if largest != index:
        # Swapping the value
        temp = heap[largest]
        heap[largest] = heap[index]
        heap[index] = temp

        # Recursively calling heapify for the changed index
        max_heapify(heap, largest, length)
    




def build_heap(heap):
    # Make the  Zero'th Element None
    heap.insert(0, None)
    # Find the length of the heap (-1 is for reducing the None element)
    length = len(heap) - 1
    # calculating the start and the last index
    from_ = floor(length/2)
    end_ = 0
    step = -1
    for i in range(from_, end_, step):
        max_heapify(heap, i, length)



if __name__ == '__main__':
    heap = [1,2,3,4,5,6]
    build_heap(heap)
    print(heap)