```python
def FindRepeatedWords(s):
    words = s.lower().split()
    freq = {}
    res = []
    for w in words:
        if w not in freq:
            freq[w] = 1
        else:
            freq[w] += 1
    for key , val in freq.items():
        if val > 1:
            res.append(key)

    return res
```