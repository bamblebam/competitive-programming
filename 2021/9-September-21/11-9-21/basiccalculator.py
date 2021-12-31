class Solution:
    def calculate(self, s: str) -> int:
        def calc(idx):
            def update(op, val):
                if op == '+':
                    stack.append(val)
                if op == '-':
                    stack.append(-val)
                if op == '*':
                    stack.append(stack.pop()*val)
                if op == '/':
                    stack.append(int(stack.pop()*val))
            num, stack, sign = 0, list(), '+'
            while idx < len(s):
                if s[idx].isdigit():
                    num = num*10+int(s[idx])
                elif s[idx] in '+-*/':
                    update(sign, num)
                    num, sign = 0, s[idx]
                elif s[idx] == '(':
                    num, j = calc(idx+1)
                    idx = j-1
                elif s[idx] == ')':
                    update(sign, num)
                    return sum(stack), idx+1
                idx += 1
            update(sign, num)
            return sum(stack)
        return calc(0)
