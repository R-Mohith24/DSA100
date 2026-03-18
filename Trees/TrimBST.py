# trim the BST to keep only the nodes in the range [low, high]

def trim(root , a , b):
    if root is None:
        return None
    if root.data < a :
        return trim(root.right , a , b)
    if root.data > b:
        return trim(root.left , a , b)

    if root.data >= a and root.data <= b:
        root.left = trim(root.left , a , b)
        root.right = trim(root.right , a , b)
    return root