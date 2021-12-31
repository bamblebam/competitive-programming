class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = list()
        stack2 = list()
        j = 0
        for i in range(len(pushed)):
            while len(stack) > 0 and stack[-1] == popped[j]:
                stack2.append(stack.pop())
                j += 1
            stack.append(pushed[i])
        for i in range(len(stack)):
            stack2.append(stack.pop())
        if popped == stack2:
            return True
        return False


sol = Solution()
print(sol.validateStackSequences([1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
