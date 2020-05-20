class MinStack:
    def __init__(self):
        self.stack = []
        self.currentMin = None
        self.length = 0

    """
     Function to push the element to stack
    """
    def push(self, x):

        """
         check the new data and assign currentMin
        """
        if self.currentMin is None or x < self.currentMin:
            self.currentMin = x

        newStackNode = stackNode(x, self.currentMin)

        self.stack.append(newStackNode)

        self.length = self.length + 1
    
    """
     pop the element from stack
    """
    def pop(self):
        self.stack.pop()
        self.length = self.length - 1 
        if self.length == 0:
            self.currentMin = None
        else:
            self.currentMin = self.getMin()

    """
      Get the top of the stack
    """
    def top(self):
        tp = self.stack[self.length - 1]
        return tp.data

    """
     Get the minimum element
    """
    def getMin(self):
        tp = self.stack[self.length - 1]
        return tp.minimun
    


        
"""
    Stack Node class
"""
class stackNode:
    def __init__(self, data, currentMin):
        self.data = data
        self.minimun = currentMin