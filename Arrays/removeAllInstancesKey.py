def remove_element(arr, key):
    next_element = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1

    return next_element




print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_element([2, 11, 2, 2, 1], 2))