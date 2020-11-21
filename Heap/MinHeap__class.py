class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self,val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)
    

    def getMin(self):
        if self.heap:
            return self.heap[0]
        
        return None

    def removeMin(self):
        if len(self.heap) > 1:
            min_ = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__minHeapify(0)
            return min_
        elif len(self.heap) == 1:
            min_ = self.heap[0]
            del self.heap[0]
            return min_
        else:
            return None

    def __percolateUp(self, index):
        parent = (index - 1) // 2

        if index <= 0:
            return
        
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.__percolateUp(parent)


    def __minHeapify(self, index):
        left = (2 * index) + 1
        right = (2 * index) + 2
        smallest = index
        
        if len(self.heap) > left and self.heap[left] < self.heap[smallest]:
            smallest = left
        if len(self.heap) > right and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.__minHeapify(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__minHeapify(i)



min__heap = MinHeap()
min__heap.buildHeap([3,4,5,1])
print(min__heap.getMin())
print(min__heap.removeMin())
print(min__heap.getMin())
print(min__heap.heap)


        
