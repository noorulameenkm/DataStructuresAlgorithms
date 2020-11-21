def minheapify(heap, index):
    left = (2 * index) + 1
    right = (2 * index) + 2
    smallest = index
    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right

    if index != smallest:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        minheapify(heap, smallest)

    return heap


"""
Time Complexity - O(n)
"""

def convertMax(maxHeap):
    for i in range(len(maxHeap) - 1, -1, -1):
        maxHeap = minheapify(maxHeap, i)
    
    return maxHeap


maxHeap = [9, 4, 7, 1, -2, 6, 5]
print(convertMax(maxHeap))
