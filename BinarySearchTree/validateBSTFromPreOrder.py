class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        root = -2 ** 32
        s = []
        
        for value in A:
            if value < root:
                return False
            
            while len(s) > 0 and s[-1] < value:
                root = s.pop()
            
            s.append(value)
            
        return True


class Solution2:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low = -1
        p = A[0]
      
        # Traverse given array 
        for value in A:  
            #NOTE:value is equal to pre[i] according to the  
            #given algo    
          
            # If we find a node who is on the right side 
            # and smaller than root, return False 
            if value < low : 
                return False 
          
            if value > p:
                low = p
    
            p = value
    
        return True



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
def buildTree(seq, index, min_, max_):
    if index == len(seq):
        return None, index
    
    val = seq[index]
    if val < min_ or val > max_:
        return None, index
    
    root = Node(val)

    index = index + 1

    root.left, index = buildTree(seq, index, min_, val - 1)
    root.right, index = buildTree(seq, index, val + 1, max_)

    return root, index

def main():
    print(Solution().solve([7, 7, 10, 10, 9, 5, 2, 8]))
    print(Solution().solve([15, 10, 8, 12, 20, 16, 25]))
    print(Solution2().solve([7, 7, 10, 10, 9, 5, 2, 8]))
    print(Solution2().solve([15, 10, 8, 12, 20, 16, 25]))
    seq = [7, 7, 10, 10, 9, 5, 2, 8]
    print(buildTree(seq, 0, float('-inf'), float('inf'))[1] == len(seq))
    seq = [15, 10, 8, 12, 20, 16, 25]
    print(buildTree(seq, 0, float('-inf'), float('inf'))[1] == len(seq))
main()