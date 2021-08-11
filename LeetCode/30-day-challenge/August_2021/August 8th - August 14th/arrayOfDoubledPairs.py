from collections import Counter

"""
    Problem Link:- https://leetcode.com/problems/array-of-doubled-pairs/
"""


def array_of_doubled_pairs(arr):
    counter = Counter(arr)

    for num in sorted(counter, key=abs):
        if counter[num * 2] < counter[num]:
            return False

        counter[num * 2] -= counter[num]
        counter[num] = 0

    return True


print(array_of_doubled_pairs(arr=[3, 1, 3, 6]))
print(array_of_doubled_pairs(arr=[2, 1, 2, 6]))
print(array_of_doubled_pairs(arr=[4, -2, 2, -4]))
print(array_of_doubled_pairs(arr=[1, 2, 4, 16, 8, 4]))
