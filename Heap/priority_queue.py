from math import floor

class PriorityQueue:
    def __init__(self):
        self.queue = [None]
        self.queueSize = 0
    
    def insert(self, el):
        self.queueSize += 1
        self.queue.insert(self.queueSize,-1)
        self.increase_val(self.queueSize,el)
        return

    def max_heapify(self,index):
        left = 2 * index
        right = 2 * index + 1
        largest = index

        if left <= self.queueSize and self.queue[left] > self.queue[largest]:
            largest = left
        
        if right <= self.queueSize and self.queue[right] > self.queue[largest]:
            largest = right
        
        if largest != index:
            temp_ = self.queue[index]
            self.queue[index] = self.queue[largest]
            self.queue[largest] = temp_

            self.max_heapify(largest)
        return 

    def get_max_val(self):
        if self.queueSize <= 0:
            raise Exception('Queue is Empty')
        
        return self.queue[1]
    
    def extract_max_val(self):
        if self.queueSize <= 0:
            raise Exception('Queue is Empty')

        val = self.queue[1]
        self.queue[1] = self.queue[self.queueSize]
        self.queueSize = self.queueSize - 1
        self.max_heapify(1)

        return val

    def increase_val(self, index, val):
        if self.queueSize <= 0:
            raise Exception('No Elements Found')
            return

        if val < self.queue[index]:
            raise Exception('Value should be greater')
            return
        
        self.queue[index] = val
        while index > 1 and self.queue[index] > self.queue[floor(index/2)]:
            temp_ = self.queue[index]
            self.queue[index] = self.queue[floor(index/2)]
            self.queue[floor(index/2)] = temp_

            index = floor(index/2)
    


def insertIntoQueue(pq, arr):
    for i in range(0, len(arr)):
        pq.insert(arr[i])



if __name__ == '__main__':
    arr = [10,1,3,20,4,9,7,6,5]
    pq = PriorityQueue()
    insertIntoQueue(pq,arr)
    print(pq.get_max_val())
    # pq.extract_max_val()
    # pq.extract_max_val()
    # pq.extract_max_val()
    print(pq.queue[1:])
