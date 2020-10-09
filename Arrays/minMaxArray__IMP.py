def max_min(lst):
    result = []
    start, end = 0, len(lst) - 1
    while start < end:
        result.append(lst[end])
        result.append(lst[start])

        start += 1
        end -= 1

    if start == end:
        result.append(lst[start])

    return result


def max_min2(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


print(max_min([1, 2, 3, 4, 5, 6, 7]))
print(max_min([1, 2, 3, 4, 5]))
print(max_min2([1, 2, 3, 4, 5, 6, 7]))
print(max_min2([1, 2, 3, 4, 5]))