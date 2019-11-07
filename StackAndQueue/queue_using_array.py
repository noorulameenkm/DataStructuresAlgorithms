class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return -1

    def dequeueAll(self):
        while len(self.queue) != 0:
            print(self.queue.pop(0), end=' ')



def Main():
    queue = Queue()
    input_list = [int(num) for num in input().split(' ') if num != '']
    for num in input_list:
        queue.enqueue(num)

    queue.dequeueAll()
    print('\n', end = '')

if __name__ == '__main__':
    Main()
