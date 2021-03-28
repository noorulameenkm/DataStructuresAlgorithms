def ternary_tree_paths(root):
      def dfs(root, current, paths):
            current.append(str(root.val))
            if all(child is None for child in root.children):
                  paths.append('->'.join(current)) 
                  return

            for child in root.children:
                  if child is not None:
                        dfs(child, current, paths)
                        current.pop()
                  
            
      current, paths = [], []
      if root:
            dfs(root, current, paths)
      return paths


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def build_tree(nodes):
    val = next(nodes)
    if not val or val == 'x': return
    cur = Node(val, [])
    for _ in range(3): cur.children.append(build_tree(nodes))
    return cur

if __name__ == '__main__':
    inputs = ["1 2 5 x x x x x 3 x x x 4 x x x", "1 2 3 x x x 4 x x x 7 x x x 5 x x x 6 x x x"]
    for i in range(len(inputs)):
        root = build_tree(iter(inputs[i].split()))
        print("Ternary tree path :",ternary_tree_paths(root))