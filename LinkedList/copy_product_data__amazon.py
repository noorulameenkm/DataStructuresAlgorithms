
class Node:
    def __init__(self, val, next=None, related=None):
        self.prod = val
        self.next = next
        self.related = related


"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def copy_product_relations(head):

    if not head:
        return head

    visited = {}
    def get_cloned_node(node):
        if not node:
            return None
        
        if node in visited:
            return visited[node]
        
        visited[node] = Node(node.prod)
        return visited[node]

    old_node = head
    new_node = Node(old_node.prod)
    visited[old_node] = new_node

    while old_node != None:
        
        # Get the clones of the nodes referenced by related and next pointers.
        new_node.related = get_cloned_node(old_node.related)
        new_node.next = get_cloned_node(old_node.next)

        old_node = old_node.next
        new_node = new_node.next

    return visited[head]


def list_to_string(lst):
    if not lst:
        return
    print("[", end=" ")
    while lst:
        print(f"(prod:{lst.prod}, related:{lst.related.prod if lst.related else None})", end=" ")
        lst = lst.next

    print("]")



head = Node(3)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.related = head.next.next
head.next.related = None
head.next.next.related = None
head.next.next.next.related = head.next
list_to_string(head)
new_head = copy_product_relations(head)
list_to_string(new_head)