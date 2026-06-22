```
from collections import deque
class Solution:
    def topView(self, root):
        if not root:
            return None
        d = {}
        q = deque()
        q.append((root,0))
        while q:
            x , col = q[0]
            q.popleft()
            
            if col not in d:
                d[col] = x.data
            
            if x.left:
                q.append((x.left , col -1))
            if x.right:
                q.append((x.right , col + 1))
                
        return [d[key] for key in sorted(d)]
```
Here we go! 🎯

Using this tree:
```
        1  (col 0)
       / \
      2   3  (col -1, col 1)
```

---

## Initial Setup

```python
d = {}
q = deque()
q.append((root, 0))
```
- `d = {}`
- `q = [(node1, 0)]`  ← root with col 0

---

## Iteration 1

```python
x, col = q[0]
q.popleft()
```
- `x = node(1)`, `col = 0`
- `q = []` ← empty after pop

```python
if col not in d:
    d[col] = x.data
```
- `0 not in {}` → True!
- `d = {0: 1}` ✅

```python
if x.left: q.append((x.left, col-1))
```
- node 1 has left child (node 2)!
- `q = [(node2, -1)]`

```python
if x.right: q.append((x.right, col+1))
```
- node 1 has right child (node 3)!
- `q = [(node2, -1), (node3, 1)]`

---

## Iteration 2

```python
x, col = q[0]
q.popleft()
```
- `x = node(2)`, `col = -1`
- `q = [(node3, 1)]`

```python
if col not in d:
    d[col] = x.data
```
- `-1 not in {0:1}` → True!
- `d = {0:1, -1:2}` ✅

```python
if x.left: q.append((x.left, col-1))
if x.right: q.append((x.right, col+1))
```
- node 2 has no children!
- `q = [(node3, 1)]` unchanged

---

## Iteration 3

```python
x, col = q[0]
q.popleft()
```
- `x = node(3)`, `col = 1`
- `q = []` ← empty!

```python
if col not in d:
    d[col] = x.data
```
- `1 not in {0:1, -1:2}` → True!
- `d = {0:1, -1:2, 1:3}` ✅

```python
if x.left: q.append((x.left, col-1))
if x.right: q.append((x.right, col+1))
```
- node 3 has no children!
- `q = []` unchanged

---

## Queue empty → exit loop!

---

## Return

```python
return [d[key] for key in sorted(d)]
```
- `sorted(d)` = `[-1, 0, 1]`
- `d[-1] = 2`
- `d[0] = 1`
- `d[1] = 3`
- **return `[2, 1, 3]`** ✅

---

Output: `2 1 3` = top view from left to right! 🎯

Does every step make sense now? 😊