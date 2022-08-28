from heapq import *

"""
    Time Complexity - O(nlogk)
    Space Complexity - O(k)
"""
def kth_highest_rank(ranks, k):
    min_heap = []

    for i in range(k):
        heappush(min_heap, ranks[i])
    
    for i in range(k, len(ranks)):
        if ranks[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, ranks[i])
    
    return min_heap[0]


# Driver code
driver_ranks = [1, 5, 12, 2, 11, 9, 7, 30, 20]
k = 3 # Supplied by a hidden API

print("Driver with the rank", kth_highest_rank(driver_ranks, k), "is selected!")