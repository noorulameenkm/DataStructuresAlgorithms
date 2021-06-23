"""
Problem Link:- https://leetcode.com/problems/reverse-linked-list-ii/
"""

class Solution:
    def reverseBetween(self, head, left, right):
        if head is None or left == right:
            return head
        
        def reverse(head_):
            if head_ is None:
                return head_

            prev_ = None
            current_ = head_
            next_ = None
            tail = current_
            while current_:
                next_ = current_.next
                current_.next = prev_
                prev_ = current_
                current_ = next_

            return prev_, tail
        
        prev = None
        after = None
        left_node = right_node = None
        current = head
        i = 1
        
        while i < left and current:
            prev = current
            current = current.next
            i += 1
        
        left_node = current
        
        while i < right and current:
            current = current.next
            i += 1
        
        right_node = current
        after = right_node.next
        
        right_node.next = None
        
        second_head, second_tail = reverse(left_node)
        
        if prev is not None:
            prev.next = second_head
            second_tail.next = after
            return head
        
        second_tail.next = after
        return second_head