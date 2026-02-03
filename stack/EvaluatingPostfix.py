def evalPostfix(str):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in str:
        if char not in operators:
            stack.append(int(char))
        else:
            second = stack.pop()
            first = stack.pop()
            if char == '+':
                stack.append(first + second)
            elif char == '-':
                stack.append(first - second)
            elif char == '*':
                stack.append(first * second)
            elif char == '/':
                stack.append(int(first / second))  # Use int() to perform floor division for negative numbers

    return stack.pop()


str = input("enter an str for postfix eval: ")
res = evalPostfix(str)
print(res)