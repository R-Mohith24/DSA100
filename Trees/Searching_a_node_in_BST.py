from NodeClass import Node

def search(root , data):
    if root is None:
        return False
    if root.data == data:
        return True
    if data < root.data:
        return search(root.left , data)
    else:
        return search(root.right , data)