from math import inf


def kth_element_of_two_sorted_array(array_1, array_2, k):
    if len(array_2) < len(array_1):
        array_1, array_2 = array_2, array_1

    n1, n2 = len(array_1), len(array_2)
    low, high = 0, min(k, n1)

    if k > n2:
        low = k - n2

    while low <= high:

        cut1 = low + (high - low) // 2
        cut2 = k - cut1

        l1 = -inf if cut1 == 0 else array_1[cut1 - 1]
        l2 = -inf if cut2 == 0 else array_2[cut2 - 1]

        r1 = inf if cut1 == n1 else array_1[cut1]
        r2 = inf if cut2 == n2 else array_2[cut2]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1

    return -1


print(kth_element_of_two_sorted_array([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))
array_1 = [100, 112, 256, 349, 770]
array_2 = [72, 86, 113, 119, 265, 445, 892]
print(kth_element_of_two_sorted_array(array_1, array_2, 7))
