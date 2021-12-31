from collections import deque


class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        queue = deque(nums)
        ans = list()
        while queue:
            if queue:
                ans.append(queue.popleft())
            if queue:
                ans.append(queue.pop())
        return ans
