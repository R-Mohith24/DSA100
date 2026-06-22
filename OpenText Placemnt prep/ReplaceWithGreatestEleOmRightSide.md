### Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.After doing so, return the array.


```
Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
```

```
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
```

```python
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)

        return arr
```


Let's dry run it **very slowly**, showing exactly what happens at each iteration.

### Input

```python
arr = [17, 18, 5, 4, 6, 1]
```

Initialize:

```python
max_right = -1
```

Since we traverse from **right to left**, we start at index `5`.

---

## Iteration 1

### i = 5

Current array:

```python
[17, 18, 5, 4, 6, 1]
```

Store current value:

```python
current = arr[5] = 1
```

Replace with `max_right`:

```python
arr[5] = -1
```

Array becomes:

```python
[17, 18, 5, 4, 6, -1]
```

Update max:

```python
max_right = max(-1, 1)
          = 1
```

State now:

```python
arr       = [17, 18, 5, 4, 6, -1]
max_right = 1
```

---

## Iteration 2

### i = 4

Current array:

```python
[17, 18, 5, 4, 6, -1]
```

Store current value:

```python
current = 6
```

Replace with `max_right`:

```python
arr[4] = 1
```

Array becomes:

```python
[17, 18, 5, 4, 1, -1]
```

Update max:

```python
max_right = max(1, 6)
          = 6
```

State now:

```python
arr       = [17, 18, 5, 4, 1, -1]
max_right = 6
```

---

## Iteration 3

### i = 3

Current array:

```python
[17, 18, 5, 4, 1, -1]
```

Store current value:

```python
current = 4
```

Replace:

```python
arr[3] = 6
```

Array becomes:

```python
[17, 18, 5, 6, 1, -1]
```

Update max:

```python
max_right = max(6, 4)
          = 6
```

State:

```python
arr       = [17, 18, 5, 6, 1, -1]
max_right = 6
```

---

## Iteration 4

### i = 2

Store:

```python
current = 5
```

Replace:

```python
arr[2] = 6
```

Array becomes:

```python
[17, 18, 6, 6, 1, -1]
```

Update max:

```python
max_right = max(6, 5)
          = 6
```

State:

```python
arr       = [17, 18, 6, 6, 1, -1]
max_right = 6
```

---

## Iteration 5

### i = 1

Store:

```python
current = 18
```

Replace:

```python
arr[1] = 6
```

Array becomes:

```python
[17, 6, 6, 6, 1, -1]
```

Update max:

```python
max_right = max(6, 18)
          = 18
```

State:

```python
arr       = [17, 6, 6, 6, 1, -1]
max_right = 18
```

---

## Iteration 6

### i = 0

Store:

```python
current = 17
```

Replace:

```python
arr[0] = 18
```

Array becomes:

```python
[18, 6, 6, 6, 1, -1]
```

Update max:

```python
max_right = max(18, 17)
          = 18
```

Final state:

```python
arr = [18, 6, 6, 6, 1, -1]
```

---

## The Core Idea

At every step:

```python
current = arr[i]      # Save original value
arr[i] = max_right    # Put answer for this index
max_right = max(max_right, current)
```

The order is **extremely important**.

If you update `max_right` first:

```python
max_right = max(max_right, arr[i])
arr[i] = max_right
```

then the current element would incorrectly consider **itself** as being on its right.

That's why we:

1. Save current value.
2. Write answer.
3. Update max.

This guarantees `max_right` always represents **the greatest element strictly to the right** of the current index. 🎯

```cpp
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i] , max_right)
            arr[i] = max_right
            max_right = newMax
        return arr
```
