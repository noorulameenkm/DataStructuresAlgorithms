class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.size() == 0 

    def size(self):
        return len(self.stack)

    def top(self):
        if self.is_empty():
            return None
        
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        
        return self.stack.pop()

    def print(self):
        if self.is_empty():
            print('Stack is Empty')
        
        print(self.stack)
    
