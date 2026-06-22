from NodeClass import Node

# inorder Traversal
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

#preorder traversal
def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

# post order traversal
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
