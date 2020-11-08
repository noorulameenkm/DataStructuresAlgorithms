from Queue import Queue
from Stack import Stack

"""
Time Complexity - O(n)
O(N)
"""

def reverseK(queue, k):
    # Write your code here
    stack = Stack()
    if k > queue.size() or k < 0:
        return None
    i = 0
    while i < k:
        stack.push(queue.dequeue())
        i += 1

    resultQueue = Queue()
    while stack.size() > 0:
        resultQueue.enqueue(stack.pop())

    while queue.size() > 0:
        resultQueue.enqueue(queue.dequeue())

    return resultQueue






def main():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)

    result = reverseK(q, 5)

    result.print()



main()