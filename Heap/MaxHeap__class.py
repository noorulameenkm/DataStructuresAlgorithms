class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)
    
    def __percolateUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__percolateUp(parent)

    def getMax(self):
        if len(self.heap) > 0:
            return self.heap[0]
        
        return None
    
    def removeMax(self):
        if len(self.heap) > 1:
            max_ = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max_
        elif len(self.heap) == 1:
            max_ = self.heap[0]
            del self.heap[0]
            return max_
        else:
            return None

    def __maxHeapify(self,index):
        left = (2 * index) + 1
        right = (2 * index) + 2
        largest = index
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(i)



max__heap = MaxHeap()
max__heap.buildHeap([1,2,3,4])
# print(max__heap.heap)
print(max__heap.getMax())
max__heap.removeMax()
print(max__heap.getMax())