def PostfixToInfix(str):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in str:
        if char in operators:
            second = stack.pop()
            first = stack.pop()
            stack.append("(" + first + char + second + ")")
        else:
            stack.append(char)
    return stack.pop()


str = input("enter an str for postfix eval: ")
res = PostfixToInfix(str)
print(res)