"""
Problem Link:- https://leetcode.com/problems/split-linked-list-in-parts/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head, k):
        if not head:
            return [None] * k

        current_head = head
        length = 0
        while current_head:
            length += 1
            current_head = current_head.next

        nodes_per_part = length // k
        remaining_nodes = length % k

        node = head
        prev = None
        i = 0
        result = [None] * k
        while node and i < k:
            result[i] = node
            l_ = nodes_per_part
            if remaining_nodes > 0:
                l_ += 1
            for j in range(0, l_):
                prev = node
                node = node.next

            prev.next = None
            remaining_nodes -= 1
            i += 1

        return result


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().splitListToParts(head, 5))
