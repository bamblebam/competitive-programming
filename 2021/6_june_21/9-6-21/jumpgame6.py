from sortedcontainers import SortedList


class Solution:
    def maxResult(self, nums, k: int) -> int:
        n = len(nums)
        dp = [0]*n
        sl = SortedList()
        for i, num in enumerate(nums):
            if len(sl) > k:
                sl.remove(dp[i-k-1])
            temp = 0
            if len(sl) > 0:
                temp = sl[-1]
            dp[i] = temp+num
            sl.add(dp[i])
        return dp[-1]
