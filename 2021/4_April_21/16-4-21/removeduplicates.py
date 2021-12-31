class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['*', 1]]
        for letter in s:
            if letter == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])
            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop()
        return ''.join(i*j for i, j in stack[1:])


sol = Solution()
print(sol.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
