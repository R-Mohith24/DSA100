from NodeClass import Node
from collections import deque


def LevelOrderTraversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        x = q[0]
        q.popleft()
        print(x.data)

        if x.left is not None:
            q.append(x.left)
        if x.right is not None:
            q.append(x.right)
        



