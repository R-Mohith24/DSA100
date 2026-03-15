from NodeClass import Node

def size(root):
    if root == None:
        return 0
    return 1 + size(root.left) + size(root.right)

def height(root):
    if root is None:
        return -1
    return max(height(root.left) , height(root.right)) + 1
    
def filldepth(root , d):
    if root == None:
        return
    root.depth = d
    filldepth(root.left , d+1)
    filldepth(root.right , d+1)