from node import Node


def PredSucc(root, data):
    if not root:
        return None
    
    if root.data == data:
        if root.left:
            temp = root.left

            while temp.right:
                temp = temp.right

            PredSucc.pred = temp
        if root.right:
            temp = root.right
            
            while temp.left:
                temp = temp.left
            
            PredSucc.succ = temp

        return True
    elif data < root.data:
        PredSucc.succ = root
        return PredSucc(root.left, data)
    else:
        PredSucc.pred = root
        return PredSucc(root.right, data)



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)

    data = 17
    PredSucc.succ = None
    PredSucc.pred = None

    result = PredSucc(root, data)
    
    if not result:
        print(f"{data} Not Found")
    else:
        if PredSucc.succ is not None:
            print(f"Successor is {PredSucc.succ.data}")
        else:
            print(f"No Successor for {data}")

        if PredSucc.pred is not None:
            print(f"Predecessor is {PredSucc.pred.data}")
        else:
            print(f"No Predecessor for {data}")