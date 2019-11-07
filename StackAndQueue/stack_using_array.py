class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        # todo

    def pop(self):
        # todo
        if len(self.stack) != 0:
            return self.stack.pop(len(self.stack) - 1)
        else:
            return -1

    def popAll(self):
        while len(self.stack) != 0:
            print(self.stack.pop(len(self.stack) - 1), end = ' ')

def Main():
    stack = Stack()
    input_list = [int(num) for num in input().split(" ") if num != '']
    for num in input_list:
        stack.push(num)

    stack.popAll()
    print('\n', end = '')
    


    
if __name__ == '__main__':
    Main()