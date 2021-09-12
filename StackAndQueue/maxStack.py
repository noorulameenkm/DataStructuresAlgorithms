from Stack import Stack


"""
    Time Complexity:-
    In the push() operation, we are setting one element in the stack, so the time complexity
    will be O(1). In the pop() operation, we are removing one element, so the time complexity
    will also be O(1). Additionally, the max_rating function only fetches the top element of
    the max stack, it will be O(1) as well.

    Space Complexity:-
    O(n)
"""


class MaxStack:
    def __init__(self):
        self.main_stack = Stack()
        self.max_stack = Stack()

    def push(self, value):
        self.main_stack.push(value)
        if self.max_stack.is_empty() or self.max_stack.top() < value:
            self.max_stack.push(value)
        else:
            self.max_stack.push(self.max_stack.top())

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    def max_rating(self):
        if not self.max_stack.is_empty():
            return self.max_stack.top()


ratings = MaxStack()
ratings.push(5)
ratings.push(0)
ratings.push(2)
ratings.push(4)
ratings.push(6)
ratings.push(3)
ratings.push(10)

print(ratings.main_stack.stack)
print("Maximum Rating: " + str(ratings.max_rating()))


ratings.pop()  # Back button effect
print("\nAfter clicking back button\n")
print(ratings.main_stack.stack)
print("Maximum value: " + str(ratings.max_rating()))
