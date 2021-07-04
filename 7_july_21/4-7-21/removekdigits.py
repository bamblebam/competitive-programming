class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = list()
        if n <= k:
            return '0'
        count = 0
        for i, c in enumerate(num):
            while stack and stack[-1] > c and k-count > 0:
                stack.pop()
                count += 1
            stack.append(c)
        while k-count > 0:
            stack.pop()
            count += 1
        return str(int("".join(stack)))
