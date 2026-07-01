```cpp
class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)
        left_sum = 0
        tot_sum = sum(arr)
        for i in range(n):
            right_sum = tot_sum - left_sum - arr[i]
            
            if left_sum == right_sum:
                return i
                
            left_sum += arr[i]
            
        return -1
```
