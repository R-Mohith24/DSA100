def getPriority(op):
    if op == '+' or op == '-': #lowest precedence
        return 1
    if op == '*' or op == '/': #second highest precedence
        return 2
    if op == '^':
        return 3 #highest precedence
    return 0


def infixToPostfix(givenStr):
    ans = ""
    ops = ['+', '-', '*', '/', '^']
    stack = []   # <-- LIST used as stack

    for ch in givenStr:

        # 1️⃣ If operand → directly to output
        if ch.isalnum():
            ans += ch

        # 2️⃣ If '(' → push to stack
        elif ch == '(':
            stack.append(ch)

        # 3️⃣ If ')' → pop till '('
        elif ch == ')':
            while stack and stack[-1] != '(': #while stack --> while stack is not empty
                ans += stack.pop()
            stack.pop()   # remove '('

        # 4️⃣ If operator
        elif ch in ops:
            while (stack and stack[-1] != '(' and
                   getPriority(stack[-1]) >= getPriority(ch)):
                ans += stack.pop()
            stack.append(ch)

    # 5️⃣ Pop remaining operators
    while stack:
        ans += stack.pop()

    return ans


# Example
givenStr = "1*(2+3)"
print(infixToPostfix(givenStr))
