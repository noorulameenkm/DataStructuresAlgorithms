class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

    print('\n', end='')

def findJoiningUsingHash(head_1, head_2):
    d = {}
    temp_1 = head_1
    temp_2 = head_2
    while temp_1:
        d[id(temp_1)] = temp_1.val
        temp_1 = temp_1.next
    
    while temp_2:
        try:
            if d[id(temp_2)]:
                return temp_2.val
        except KeyError:
            d[id(temp_2)] = temp_2.val
        finally:
            temp_2 = temp_2.next

    return 'Doesn\'t Exist'


def findJoiningUsingArray(head_1, head_2):
    arr = []

    temp_1 = head_1
    temp_2 = head_2

    while temp_1:
        arr.append(id(temp_1))
        temp_1 = temp_1.next

    while temp_2:
        if id(temp_2) in arr:
            return temp_2.val
        
        temp_2 = temp_2.next

    return 'Doesn\'t Exist'
       



if __name__ == '__main__':
    head_1 = Node(1)
    head_1.next = Node(2)
    head_1.next.next = Node(3)
    head_2 = Node(10)
    head_2.next = Node(9)
    head_2.next.next = head_1.next.next.next = Node(5)
    head_1.next.next.next.next = Node(11)
    head_1.next.next.next.next.next = Node(12)
    print(findJoiningUsingHash(head_1, head_2))
    print(findJoiningUsingArray(head_1, head_2))
    