```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = []
        for c in s:
            if c.isalnum():
                newstr.append(c.lower())
        newstr = ''.join(newstr)
        return newstr == newstr[::-1]
```
