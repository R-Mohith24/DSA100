Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'` determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
```
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Example 5:

Input: s = "([)]"
Output: false
```

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(' , '[' ,  "{"):
                stack.append(i)
            else:
                if stack  and (stack[-1] == '(' and i == ')' or stack[-1] == '[' and i == ']' or stack[-1] == '{' and i == "}"):
                    stack.pop()

                else:
                    return False
            
        if not stack: #if stack is empty
            return True 
        else:
            return False

```
#### More readable version

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            else:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        return not stack
```


In a dictionary, 
`pairs = {')': '(', ...}` — the thing before the colon is the key, the thing after the colon is the value. So here, `')'` is the key, and `'('` is its value.

To look something up, you write `pairs[something]`, and Python finds the matching value for that key. So `pairs[')']` would give you back `'('`

when you see an opening bracket, you don't need to look anything up — you just push it. It's only when you see a closing bracket that you need to ask "what opening bracket should be sitting on top of the stack right now?"
