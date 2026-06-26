## Find All Anagrams in a String
---

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

 
```
Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```
```python

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        Pcount , Scount = {} , {}
        for i in range(len(p)):
            Pcount[p[i]] = Pcount.get(p[i] , 0) + 1
            Scount[s[i]] = Scount.get(s[i] , 0) + 1

        res = [0] if (Pcount) == (Scount) else []

        left = 0
        for right in range(len(p) , len(s)):
            Scount[s[right]] = Scount.get(s[right] , 0) + 1
            Scount[s[left]] -= 1

            if Scount[s[left]] == 0:
                Scount.pop(s[left])
            left += 1
            if (Scount) == (Pcount):
                res.append(left)

        return res

```
```
Build frequency of p.
Build frequency of first window of s.

If equal → answer = 0.

Now slide:

1. Add new character.
2. Remove old character.
3. If frequency becomes 0, remove the key.
4. Compare the two dictionaries.
5. If equal, record the left index.
```




**https://www.youtube.com/watch?v=G8xtZy0fDKg**