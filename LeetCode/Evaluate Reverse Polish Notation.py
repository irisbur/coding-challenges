from typing import List


def evalRPN(tokens: List[str]) -> int:
    operators = ["+", "-", "*", "/"]
    stack = []

    for t in tokens:
        if t in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            if t == "+":
                res = num1 + num2
            elif t == "-":
                res = num2 - num1
            elif t == "*":
                res = num2 * num1
            elif t == "/":
                res = int(num2 / num1)
            stack.append(res)
        else:
            stack.append(int(t))
    return stack[0]

