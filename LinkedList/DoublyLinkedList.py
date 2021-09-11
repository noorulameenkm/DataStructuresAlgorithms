
# Doubly linked list Nodes
class LinkedListNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, key, data):
        new_node = LinkedListNode(key, data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert_at_tail(self, key, data):
        new_node = LinkedListNode(key, data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def remove_node(self, node):
        if node is None:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev

        self.size -= 1

        return node

    def remove_head(self):
        return self.remove_node(self.head)

    def remove_tail(self):
        return self.remove_node(self.tail)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
