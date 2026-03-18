# check if the given tree is a valid binary search tree (BST)
def isValidBST(root):
    prev = None
    def inorder(node):
        nonlocal prev
        if node is None:
            return True

        left = inorder(node.left)  # go left
        if not left:   #if left == False
            return False
    
        if prev is not None and node.val <= prev:  # check current vs prev
            return False
        prev = node.val  # update prev

    return inorder(node.right)  # go right

