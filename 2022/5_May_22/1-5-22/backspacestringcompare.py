class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(x):
            stack=list()
            for c in x:
                if c=="#" and stack:
                    stack.pop()
                elif c!="#":
                    stack.append(c)
            return "".join(stack)
        return helper(s)==helper(t)