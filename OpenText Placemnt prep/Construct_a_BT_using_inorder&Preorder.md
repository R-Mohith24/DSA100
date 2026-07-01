


```python
def buildtree(preorder : List[int] , inorder : List[int]):
    if not preorder  or not inorder :
        return None
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = buildtree(preorder[1:idx+1] , inorder[:idx])
    root.right = buildtree(preorder[idx+1:] , inorder[idx+1:])
    return root
```
