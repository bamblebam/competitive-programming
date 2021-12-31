class Solution:
    def evalRPN(self, tokens) -> int:
        ops = '+-*/'
        stack = list()

        def operate(a, b, op):
            if op == '+':
                return a+b
            if op == '-':
                return a-b
            if op == '*':
                return a*b
            if op == '/':
                return int(a/b)
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(operate(a, b, token))
            else:
                stack.append(int(token))
        return stack[-1]
