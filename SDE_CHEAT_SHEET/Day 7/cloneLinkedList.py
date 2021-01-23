"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        
        if not head:
            return None
        
        iter_ = head
        newhead = None
        newtail = None
        
        while iter_:
            node = Node(iter_.val)
            
            temp = iter_.next
            iter_.next = node
            node.next = temp
        
            iter_ = temp
        
        iter_ = head
        while iter_:
            if iter_.random:
                iter_.next.random = iter_.random.next
                
            iter_ = iter_.next.next
        
        iter_ = head
        while iter_:    
            node = iter_.next
            
            iter_.next = node.next
            
            if newhead is None:
                newhead = node
                newtail = newhead
            else:
                newtail.next = node
                newtail = newtail.next
            
            iter_ = iter_.next
        
        return newhead
                
        