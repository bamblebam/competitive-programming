class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for x in S:
            if x == "(":
                stack.append(0)
            else:
                value = stack.pop()
                stack[-1] += max(2*value, 1)
        return stack[0]


sol = Solution()
print(sol.scoreOfParentheses("(()(()))"))
