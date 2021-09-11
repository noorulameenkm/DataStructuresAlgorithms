from DoublyLinkedList import LinkedList


"""
    Time Complexity:- O(1)
    Space Complexity - O(k)

    Time Complexity
        We know that the time complexity of this solution is constant, O(1) because
        of these complexities:

        Get (HashMap): Constant, O(1)

        Set (HashMap): Constant, O(1)

        Addition, deletion from the head and tail of LinkedList: Constant, O(1)O(1)

    Space complexity
        The memory complexity of this solution is, O(k), where k is the size of the cache.
"""


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.cache_vals = LinkedList()

    def Set(self, key, value):
        if key not in self.cache:
            if self.cache_vals.size >= self.capacity:
                self.cache_vals.insert_at_tail(key, value)
                self.cache[key] = self.cache_vals.get_tail()
                del self.cache[self.cache_vals.get_head().key]
                self.cache_vals.remove_head()
            else:
                self.cache_vals.insert_at_tail(key, value)
                self.cache[key] = self.cache_vals.get_tail()
        else:
            self.cache_vals.remove_node(self.cache[key])
            self.cache_vals.insert_at_tail(key, value)
            self.cache[key] = self.cache_vals.get_tail()

    def Get(self, key):
        if key not in self.cache:
            return None
        else:
            value = self.cache[key].data
            self.cache_vals.remove_node(self.cache[key])
            self.cache_vals.insert_at_tail(key, value)
            self.cache[key] = self.cache_vals.get_tail()
            return value

    def print_data(self):
        node = self.cache_vals.get_head()
        while node is not None:
            print("(" + str(node.key) + "," + str(node.data) + ")", end="")
            node = node.next
        print()


# Driver code
print("The most recent wathced titles are: (key, value)")
obj = LRU(3)
obj.Set(10, 20)
obj.print_data()

obj.Set(15, 25)
obj.print_data()

obj.Set(20, 30)
obj.print_data()

obj.Set(25, 35)
obj.print_data()

obj.Set(5, 40)
obj.print_data()

obj.Get(25)
obj.print_data()
