
So the LCA is just the **last node that appears in both paths** before they diverge!

You already have the while loop that finds where paths diverge:

```python
while p1 < len(ls1) and p2 < len(ls2) and ls1[p1] == ls2[p2]:
    p1 += 1
    p2 += 1
```

After this loop, `p1` and `p2` point to where they **stopped matching**.

So the LCA is at index... `p1 - 1` or `p2 - 1`! 🎯

```python
lca = ls1[p1 - 1]
```

That's it! Your `findDist` code **already finds LCA internally** — you just never returned it!

So LCA function is literally:
```
def path(root : Optional[TreeNode] , x : Optional[TreeNode] , ls : List[int]) -> bool:
    if root == None:
        return False
    if root.val == x or path(root.left , x , ls) == True or path(root.right , x , ls) == True :
        ls.append(root)
        return True
    return False
```

```python
def findLCA(root, a, b):
    ls1, ls2 = [], []
    path(root, a, ls1)
    path(root, b, ls2)
    ls1.reverse()
    ls2.reverse()
    p1 = p2 = 0
    while p1 < len(ls1) and p2 < len(ls2) and ls1[p1].data == ls2[p2].data:
        p1 += 1
        p2 += 1
    return ls1[p1 - 1]  # last common node = LCA!
```
