## Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without duplicate characters.

 
```
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

---
---

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        hashset = set()
        n = len(s)
        for r in range(n):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1

            hashset.add(s[r])

            max_len = max(max_len , r - l +1)
        return max_len

```


The way to remember it forever is:

> **Expand → Fix → Record**

### 1. Expand the window

```python
hashset.add(s[r])
```

Every iteration, we try to include a new character.

---

### 2. Fix the window

Before adding, we check:

```python
while s[r] in hashset:
```

If the new character already exists, the window becomes invalid because it has duplicates.

So we **keep removing characters from the left** until the duplicate disappears.

```python
hashset.remove(s[l])
l += 1
```

Notice it's a **while**, not an **if**.

Why?

Because there might be several characters to remove before the duplicate is gone.

---

### 3. Record the answer

Now the window is valid again:

```text
All characters are unique.
```

So we update:

```python
max_len = max(max_len, r - l + 1)
```

---

## The mental model 🧠

```text
Expand window
      ↓
Duplicate?
      ↓
Yes → Keep shrinking until no duplicate
      ↓
Window is valid
      ↓
Update answer
      ↓
Repeat
```

### Sliding Window Cheat Sheet

* **Fixed size** → Grow → Shrink once → Process
* **Variable size (sum)** → Grow → While valid → Process → Shrink
* **Variable size (duplicates)** → Grow → While invalid → Shrink → Process

