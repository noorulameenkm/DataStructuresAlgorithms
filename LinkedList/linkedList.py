class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
    
    def getVal(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.root = None 

    ''' 
        Code to add node to the linkedlist
    '''
    def addNode(self, nodeVal):
        newNode = Node(nodeVal)
        if self.root is None:
            self.root = newNode
        else:
            temp_root = self.root
            while temp_root.next is not None:
                temp_root = temp_root.next
            temp_root.next = newNode

    ''' 
        Code to add node to the beginning of the linked list
    '''
    def addNodetoBeginning(self, nodeVal):
        newNode = Node(nodeVal)
        newNode.next = self.root
        self.root = newNode 

    ''' 
        Code to delete node from the linkedlist
    '''
    def deleteNode(self, data):
        temp_node = self.root
        temp_previous = self.root 
        deleted = False 
        while temp_node is not None and deleted is not True:
            if temp_node.getVal() == data:
                if temp_node is self.root:
                    self.root = temp_node.next
                    deleted = True  
                    break
                else:
                    temp_previous.next = temp_node.next
                    deleted = True 
                    break 
            
            temp_previous = temp_node 
            temp_node = temp_node.next
        
        if deleted is not True:
            print("The value {0} is not found in the linked list".format(data))

    ''' 
        Code to print the linkedlist
    '''
    def printList(self):
        temp_root = self.root 
        while temp_root is not None:
            print(temp_root.getVal(), end=' ')
            temp_root = temp_root.next
        print('\n', end='')
            


            
''' 
    Main function
'''
def Main():
    linkedList = LinkedList()
    input_string = input("Enter the elements that you want to add to the linked list\n")
    for el in input_string.split(" "):
        try:
            linkedList.addNode(int(el))
        except:
            pass
        
    linkedList.printList()




if __name__ == '__main__':
    Main()





