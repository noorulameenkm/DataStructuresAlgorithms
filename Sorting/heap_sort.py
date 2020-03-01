from math import floor


def max_heapify(array, index, length):
    left = 2 * index
    right = 2 * index + 1

    largest = index

    if left <= length and array[left] > array[largest]:
        largest = left
    if right <= length and array[right] > array[largest]:
        largest = right

    if largest != index:
        temp_ = array[index]
        array[index] = array[largest]
        array[largest] = temp_

        max_heapify(array, largest, length)

def build_max_heap(array):
    # Make the 0th element None
    array.insert(0, None)
    length = len(array) - 1

    from_ = floor(length/2)
    to_ = 0
    step_ = -1
    for i in range(from_, to_, step_):
        max_heapify(array, i, length)

def heap_sort(array):
    build_max_heap(array)
    length = len(array) - 1
    from_ = len(array) - 1
    to_ = 1
    step_ = -1
    for i in range(from_, to_, step_):

        #swap with the last element
        temp_ = array[length]
        array[length] = array[1]
        array[1] = temp_

        # decrement the length
        length -= 1

        max_heapify(array, 1, length)


if __name__ == '__main__':
    array = [5,3,4,10,2,9,12,1,8]
    heap_sort(array)
    out_ = array[1:]
    print(out_)