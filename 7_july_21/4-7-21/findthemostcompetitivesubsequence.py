class Solution:
    def mostCompetitive(self, nums, k: int):
        stack = list()
        n = len(nums)
        for i, c in enumerate(nums):
            while stack and stack[-1] > c and len(stack)-1+n-i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(c)
        return stack
