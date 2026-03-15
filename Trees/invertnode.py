from NodeClass import Node

def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp

    return