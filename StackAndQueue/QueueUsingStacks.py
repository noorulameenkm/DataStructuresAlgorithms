from Stack import Stack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = Stack()
        # Write your code here
        self.stack_ = Stack()

        # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value)
        return True
        
        
    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        while self.main_stack.size() != 0:
            self.stack_.push(self.main_stack.pop())
        
        returnVal = self.stack_.pop()
        while self.stack_.size() != 0:
            self.main_stack.push(self.stack_.pop())

        return returnVal




class NewQueue2:
    def __init__(self):
        # Can use size from argument to create stack
        self.main_stack = Stack()
        self.temp_stack = Stack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
            return True
        else:
            while self.main_stack.is_empty() is False:
                tmep = self.main_stack.pop()
                self.temp_stack.push(tmep)
            self.main_stack.push(value)
            while self.temp_stack.is_empty() is False:
                temp = self.temp_stack.pop()
                self.main_stack.push(temp)
            return True

    # Removes Element From Queue
    def dequeue(self):
        if not self.main_stack.is_empty():
            value = self.main_stack.pop()
            return value
        # If stack empty then return None
        return None  





def main():
    newQueue = NewQueue()
    newQueue.enqueue(1)
    newQueue.enqueue(2)
    newQueue.enqueue(3)
    newQueue.enqueue(4)

    print(newQueue.dequeue())

    newQueue.enqueue(5)
    print(newQueue.dequeue())


    newQueue2 = NewQueue2()
    newQueue2.enqueue(1)
    newQueue2.enqueue(2)
    newQueue2.enqueue(3)
    newQueue2.enqueue(4)

    print(newQueue2.dequeue())

    newQueue2.enqueue(5)
    print(newQueue2.dequeue())

main()