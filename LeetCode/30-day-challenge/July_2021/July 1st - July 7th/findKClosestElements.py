from heapq import *


class Element:
    def __init__(self, number, x):
        self.number = number
        self.diff = abs(number - x)
    
    def __lt__(self, other):
        if self.diff == other.diff:
            return self.number > other.number
        
        return self.diff > other.diff


def find_k_closest_elements(arr, k, x):
    
    results = []
    max_heap = []
    for num in arr:
        heappush(max_heap, Element(num, x))

        if len(max_heap) > k:
            heappop(max_heap)
    
    while len(max_heap) > 0:
        element = heappop(max_heap)
        results.append(element.number)
    
    results.sort()

    return results


def find_k_closest_elements_2(arr, k, x):
    results = []

    low, high = 0, len(arr) - 1

    while high - low >= k:
        if abs(arr[low] - x) > abs(arr[high] - x):
            low += 1
            continue

        high -= 1

    for i in range(low, high + 1):
        results.append(arr[i])
    
    return results



# Method 1
print(find_k_closest_elements(arr = [1,2,3,4,5], k = 4, x = 3))
print(find_k_closest_elements(arr = [1,2,3,4,5], k = 4, x = -1))


# Method 2
print(find_k_closest_elements_2(arr = [1,2,3,4,5], k = 4, x = 3))
print(find_k_closest_elements_2(arr = [1,2,3,4,5], k = 4, x = -1))