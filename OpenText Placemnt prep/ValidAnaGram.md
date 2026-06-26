Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 
```
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true
```

```
Example 2:

Input: s = "rat", t = "car"

Output: false
```
 

**Constraints**:
```
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
```


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}

        for val in s:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1
        for val in t:
            hashmap[val] = hashmap.get(val,0) - 1

        for val in hashmap.values():
            if val != 0:
                return False
        return True
```