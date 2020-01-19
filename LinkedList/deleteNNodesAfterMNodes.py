class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printList(lst):
    while lst:
        print(lst.val, end=' ')
        lst = lst.next
    
    print('\n', end='')

def getNPlusOnethNode(lst, N):
    curr = lst

    while curr and N > 0:
        curr = curr.next
        N -= 1

    if N == 0:
        return curr
    else:
        return lst



def isNNodesThere(lst, N):
    curr = lst

    while curr and N > 0:
        curr = curr.next
        N -= 1


    if N == 0:
        return True
    else:
        return False

def deleteNMNodes(lst, M, N):
    if M <= 0:
        return None

    curr = lst
    while curr and isNNodesThere(curr, M):
        Mth = getNPlusOnethNode(curr, M - 1)
        if isNNodesThere(Mth.next, N):
            NPlusOneth = getNPlusOnethNode(Mth.next, N)
        else:
            break
        
        Mth.next = NPlusOneth
        curr = NPlusOneth

    return lst


if __name__ == '__main__':
    lst = Node(1)
    lst.next = Node(2)
    lst.next.next = Node(3)
    lst.next.next.next = Node(4)
    lst.next.next.next.next = Node(5)
    lst.next.next.next.next.next = Node(6)
    lst.next.next.next.next.next.next = Node(7)
    lst.next.next.next.next.next.next.next = Node(8)
    printList(lst)
    N = 2
    M = 2
    lst = deleteNMNodes(lst, M, N)
    printList(lst)




