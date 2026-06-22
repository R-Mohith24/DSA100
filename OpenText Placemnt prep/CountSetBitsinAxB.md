**The question: given two integers A and B, compute the product A × B, then count the number of set bits (1s) in the binary representation of that product.**
```
Example: A = 3, B = 5 → product = 15 → binary of 15 = 1111 → set bits = 4
```
```python
def count_set_bits(A,B):
    P = A * B
    count = 0
    while P>0:
        if P & 1 == 1:   # checks if the last bit is 1 or not
            count += 1
        P = P >> 1   
        #right shift .. meaning it discards the rightmost bit and replaces it with the adjacent bits

    return count
```
