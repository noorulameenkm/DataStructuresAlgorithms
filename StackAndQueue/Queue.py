class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if not self.is_empty():
            return self.queue[-1]
        
        return None
    
    def back(self):
        if not self.is_empty():
            return self.queue[0]
        
        return None

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        
        return None

    def clear(self):
        self.queue = []

    def print(self):
        if self.is_empty():
            print('Queue is Empty')
        
        print(self.queue)

    
