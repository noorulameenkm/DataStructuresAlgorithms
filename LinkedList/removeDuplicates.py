class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


def printList(head):
    while head.next_element:
        print(head.data, end='->')
        head = head.next_element
    
    if head:
        print(head.data)

def remove_duplicates(head):
    # Write - Your - Code
    frequency = {}
    prev, current = head, head
    if head is None:
        return None
    while current:
        value = current.data

        if value not in frequency:
           frequency[value] = 0

        frequency[value] += 1

        if frequency[value] > 1:
            current = current.next_element
            prev.next_element = current
        else:
            prev = current
            current = current.next_element
        
    return head



def main():
    head = Node(1)
    head.next_element = Node(2)
    head.next_element.next_element = Node(2)
    head.next_element.next_element.next_element = Node(2)
    head.next_element.next_element.next_element.next_element = Node(3)
    head.next_element.next_element.next_element.next_element.next_element = Node(4)
    head.next_element.next_element.next_element.next_element.next_element.next_element = Node(4)
    head.next_element.next_element.next_element.next_element.next_element.next_element.next_element = Node(5)
    head.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element = Node(6)

    printList(head)

    head = remove_duplicates(head)

    printList(head)


main()


