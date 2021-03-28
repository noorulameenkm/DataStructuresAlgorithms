def serialize(root):
      # WRITE YOUR BRILLIANT CODE HERE
      arr = []
      def dfs(root):
            if not root:
                  arr.append('x')
                  return 
            
            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

      
      dfs(root)
      return ' '.join(arr)


class Node:
      def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

def deserialize(s):
      # WRITE YOUR BRILLIANT CODE HERE
      def dfs(nodes):
            val = next(nodes)
            if val == 'x':
                  return 
            
            curr = Node(val)
            curr.left = dfs(nodes)
            curr.right = dfs(nodes)

            return curr
      
      return dfs(iter(s.split()))


def build_tree(nodes):
      val = next(nodes)
      if not val or val == 'x': return
      cur = Node(int(val))
      cur.left = build_tree(nodes)
      cur.right = build_tree(nodes)
      return cur

def get_tree(root, arr):
      if not root: 
            arr.append("x")
            return
      arr.append(root.val)
      get_tree(root.left, arr)
      get_tree(root.right, arr)

if __name__ == "__main__":
    inputs = ["6 4 3 x x 5 x x 8 x x", "1 2 x x 3 x x", "10 86 x x 100 x x", "x"]
    for i in range(len(inputs)):
        root = build_tree(iter(inputs[i].split()))
        actual_output = deserialize(serialize(root))
        arr =[]
        get_tree(actual_output, arr)
        print("Serializing and deserializing :",' '.join(str(v) for v in arr))