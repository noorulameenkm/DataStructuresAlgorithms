"""
    Problem Link:- https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""


from heapq import *

class Element:
    def __init__(self, el):
        self.element = el
    
    def __lt__(self, other):
        return self.element > other.element



def Kth_smallest_element_sorted_matrix(matrix, k):
    min_heap = []
    for one_d in matrix:
        for num in one_d:
            heappush(min_heap, Element(num))
            if len(min_heap) > k:
                heappop(min_heap)

    return min_heap[0].element


def find_rank(sorted_matrix, target):
    count = 0 
    N = len(sorted_matrix)
    i, j = N - 1, 0

    while i >= 0 and j < N:
        if sorted_matrix[i][j] > target:
            i -= 1
            continue

        count += (i + 1)
        j += 1
    
    return count


def Kth_smallest_element_sorted_matrix_binary_search(matrix, k):
    m, n = len(matrix), len(matrix[0])
    low, high = matrix[0][0], matrix[m - 1][n - 1]

    while low < high:
        mid = low + (high - low) // 2
        rank = find_rank(matrix, mid)
        if rank < k:
            low = mid + 1
        else:
            high = mid
    
    return low


# 1st Approach
print(Kth_smallest_element_sorted_matrix(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(Kth_smallest_element_sorted_matrix(matrix = [[-5]], k = 1))


#2nd Approach
print(Kth_smallest_element_sorted_matrix_binary_search(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(Kth_smallest_element_sorted_matrix_binary_search(matrix = [[-5]], k = 1))