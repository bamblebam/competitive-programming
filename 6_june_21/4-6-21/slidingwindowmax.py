from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        ans = list()
        queue = deque()
        n = len(nums)
        for i in range(n):
            if queue and queue[0][1] <= i-k:
                queue.popleft()
            while(queue and queue[-1][0] < nums[i]):
                queue.pop()
            queue.append((nums[i], i))
            if i >= k-1:
                ans.append(queue[0][0])
        return ans
