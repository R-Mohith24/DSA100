# no . of opening and closing paranthesis should be equal
# opening paranthesis should appear before closing paranthesis
# Among different types of paranthesis, the closing paranthesis should match the last opened paranthesis.
# ex: ( [ ] ) { } --> valid
# ex: ( [ ) ] --> invalid
# ex : ( [ { } ] ) --> valid

def isValid(s):
    stack = []
    n = len(s)
    for i in range(n):
        if s[i] in ['(','{','[']:
            stack.append(s[i])
        else:
            if stack and (stack[-1] == '(' and s[i] == ')' or
                          stack[-1] == '{' and s[i] == '}' or
                          stack[-1] == '[' and s[i] == ']'):
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True