```
def path(root : Optional[TreeNode] , x : Optional[TreeNode] , ls : List[int]) -> bool:
    if root == None:
        return False
    if root == x or path(root.left , x , ls) == True or path(root.right , x , ls) == True :
        ls.append(root)
        return True
    return False

def findPathLenght(root : Optional[TreeNode] , x: Optional[TreeNode] , y:Optional[TreeNode]):
    ls1 = []
    ls2 = []
    path(root, x , ls1)
    path(root , y , ls2)
    ls1.reverse()
    ls2.reverse()
    p1 = 0
    p2 = 0
    while p1 < len(ls1) and p2 < len(ls2) and ls1[p1] == ls2[p2] : 
        p1 += 1
        p2 += 1
    return (len(ls1) - p1) + (len(ls2) - p2)
```





Let's trace through this step by step! 🎯

Using this tree, X=4, Y=5:

```
        1
       / \
      2   3
     / \
    4   5
```

---

## Step 1: `path(root=1, x=4, ls1=[])`

```python
if root == None:  # 1 is not None, skip
if root == x:     # 1 == 4? No
```
So we check `path(root.left, x, ls)` → goes to **node 2**

---

## Step 2: `path(root=2, x=4, ls1=[])`

```python
if root == None:  # 2 is not None, skip
if root == x:     # 2 == 4? No
```
Check `path(root.left, x, ls)` → goes to **node 4**

---

## Step 3: `path(root=4, x=4, ls1=[])`

```python
if root == None:  # 4 is not None, skip
if root == x:     # 4 == 4? YES! ✅
    ls.append(4)  # ls1 = [4]
    return True
```

---

## Back to Step 2: `path(root=2)`

`path(root.left)` returned `True` → short circuit, skip right!

```python
ls.append(2)  # ls1 = [4, 2]
return True
```

---

## Back to Step 1: `path(root=1)`

`path(root.left)` returned `True` → short circuit, skip right!

```python
ls.append(1)  # ls1 = [4, 2, 1]
return True
```

---

## After `ls1.reverse()`:
```
ls1 = [1, 2, 4]  ✅
```

---

## Step 4: `path(root=1, x=5, ls2=[])`

```python
if root == x:  # 1 == 5? No
```
Check left → goes to **node 2**

---

## Step 5: `path(root=2, x=5, ls2=[])`

```python
if root == x:  # 2 == 5? No
```
Check left → goes to **node 4**

---

## Step 6: `path(root=4, x=5, ls2=[])`

```python
if root == x:  # 4 == 5? No
path(root.left) → None → False
path(root.right) → None → False
return False  # 5 not found here!
```

---

## Back to Step 5: `path(root=2)`

Left returned `False` → check right → goes to **node 5**

---

## Step 7: `path(root=5, x=5, ls2=[])`

```python
if root == x:  # 5 == 5? YES! ✅
    ls.append(5)  # ls2 = [5]
    return True
```

---

## Back to Step 5: `path(root=2)`

Right returned `True`!

```python
ls.append(2)  # ls2 = [5, 2]
return True
```

---

## Back to Step 4: `path(root=1)`

Left returned `True` → short circuit!

```python
ls.append(1)  # ls2 = [5, 2, 1]
return True
```

---

## After `ls2.reverse()`:
```
ls2 = [1, 2, 5]  ✅
```

---

## Step 8: Finding common nodes

```
ls1 = [1, 2, 4]
ls2 = [1, 2, 5]
p1 = 0, p2 = 0
```

**Iteration 1:**
```
ls1[0]=1 == ls2[0]=1? YES → p1=1, p2=1
```

**Iteration 2:**
```
ls1[1]=2 == ls2[1]=2? YES → p1=2, p2=2
```

**Iteration 3:**
```
ls1[2]=4 == ls2[2]=5? NO → stop!
```

---

## Step 9: Return

```python
return (len(ls1) - p1) + (len(ls2) - p2)
     = (3 - 2)      + (3 - 2)
     = 1 + 1
     = 2 ✅
```

---

```
        1
       / \
      2   3
     / \
    4   5
```

Path: `4 → 2 → 5` = **2 edges** 🎯


