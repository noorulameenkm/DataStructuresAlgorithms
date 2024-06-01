from typing import Callable


"""
Problem link: https://leetcode.com/problems/print-in-order/description/
"""

class Foo:

    def __init__(self):
        self.current = None


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.current = "First"


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.current != "First":
            continue

        printSecond()
        self.current = "Second"


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.current != "Second":
            continue

        printThird()
        self.current = "Third"
