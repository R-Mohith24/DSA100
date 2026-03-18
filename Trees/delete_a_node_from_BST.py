'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def delNode(self, root, x):
        if root is None:
            return None
        #traversing till we find X
        
        if x < root.data:
            root.left = self.delNode(root.left,x)
        elif x > root.data:
            root.right = self.delNode(root.right,x)
        #found the x
        else:
            #case 1 - leaf Node
            
            if root.right is None and root.left is None:
                return None
                
            #case 2 - single child
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
                
            #case 3 - 2 children 
            else: #replacing root with min(root.right)
                node = root.right
                while node.left is not None:
                    node = node.left
                root.data = node.data
                root.right = self.delNode(root.right , node.data)
        return root
            
        