from NodeClass import Node

def insert(root , data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left , data)
    else:
        root.right = insert(root.right , data)
    return root

