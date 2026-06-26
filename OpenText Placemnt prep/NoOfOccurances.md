```python
def countOccurances(arr):
    hashmap = {}
    for i in arr:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    return hashmap
```
