"""
    Way of solving this problem:- 
    * i = 0
    * i % k == 0 (means jumped k nodes, that's why it is starting from i = 0)
    * in the above case assign fractional node to head
    * 2nd condition will be true in the case of i = 0 as well
      that means atleast one node is there so we have to assign 
      it to firstNode
    * Next case is when i = k which means k + 1th node, then move
      fractional Node to next Node, because more than k nodes are there
      since we are taking ceil, we can move it to next node
    * Basic idea is to jump k times and then move fractional Node to 
      the next, Do the same till completely parse list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def findFractionalNode(head, k):
    if k <= 0:
        return None
    
    fractionalNode = None
    temp = head
    i = 0
    while temp:
        if i % k == 0:
            if not fractionalNode:
                fractionalNode = head
            else:
                fractionalNode = fractionalNode.next

        temp = temp.next
        i += 1
    
    return fractionalNode

def Main(head):
    k = int(input())
    node = findFractionalNode(head, k)
    if node:
        print(node.val)
    else:
        print('No Fractional Node')

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    Main(head)
