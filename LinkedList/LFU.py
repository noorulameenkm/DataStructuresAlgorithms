from collections import defaultdict


"""
    Time Complexity
        We know that the time complexity of this solution is constant, O(1), because of these
        complexities:

        Get (HashSet): Constant, O(1)

        Set (HashSet): Constant, O(1)

        Deletion at the head when adding a new element (linked list): Constant, O(1)

        Adding a new element to tail (linked list): O(1)

    Space complexity
        The memory complexity of this solution is linear, O(n), where n is the capacity
        of the cache.
"""


class ListNode:
    def __init__(self, key, val, freq):
        self.key = key
        self.freq = freq
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        node.next, node.prev = None, None
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.next, node.prev = None, None


class LFU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_dict = {}
        self.freq_dict = defaultdict(LinkedList)

    def Get(self, key):
        if key not in self.key_dict:
            return None

        temp = self.key_dict[key]
        self.key_dict[key] = ListNode(key, temp.val, temp.freq)
        self.freq_dict[temp.freq].delete(temp)
        if not self.freq_dict[self.key_dict[key].freq].head:
            del self.freq_dict[self.key_dict[key].freq]
            if self.min_freq == self.key_dict[key].freq:
                self.min_freq += 1

        self.key_dict[key].freq += 1
        self.freq_dict[self.key_dict[key].freq].append(self.key_dict[key])
        return self.key_dict[key].val

    def Set(self, key, val):
        if self.Get(key):
            self.key_dict[key].val = val
            return

        if self.size == self.capacity:
            del self.key_dict[self.freq_dict[self.min_freq].head.key]
            self.freq_dict[self.min_freq].delete(self.freq_dict[self.min_freq].head)
            if not self.freq_dict[self.min_freq].head:
                del self.freq_dict[self.min_freq]

            self.size -= 1

        self.min_freq = 1
        self.key_dict[key] = ListNode(key, val, self.min_freq)
        self.freq_dict[self.key_dict[key].freq].append(self.key_dict[key])
        self.size += 1

    def printDict(self):
        for k, v in self.key_dict.items():
            print("(" + str(k) + ", " + str(v.val) + ")", end="")

        print("")


print("The most frequently watched titles are: (key, value)")
obj = LFU(2)
obj.Set(10, 20)
obj.Set(15, 25)
obj.Get(10)
obj.printDict()
obj.Set(20, 30)
obj.Get(15)
obj.printDict()
obj.Set(25, 35)
obj.Get(10)
obj.Get(20)
obj.Get(25)
obj.printDict()
