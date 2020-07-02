# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def bstFromPreorder(self, preorder):
        inorder = sorted(preorder)
        start = 0 
        end = len(inorder) - 1
        
        root = self.construct_bst(preorder, inorder, start, end)
        
        return root
        
        
        
        
    def construct_bst(self, preorder, inorder, start, end):
        if start <= end:
            el = preorder.pop(0)
            root = TreeNode(el)
            index = self.b_search(inorder, start, end, el)
            root.left = self.construct_bst(preorder, inorder, start, index - 1)
            root.right = self.construct_bst(preorder, inorder, index + 1, end)

            return root
        else:
            return None        
    
    
    def b_search(self, array, start, end, el):
        while start <= end:
            mid = start + (end - start)//2
            if array[mid] == el:
                return mid
            elif el > array[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        