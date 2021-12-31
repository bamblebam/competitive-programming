class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp = [0]*(n-1)
        dp2 = [0]*n
        for i in range(n-1):
            two_back = 0 if i-2 < 0 else dp[i-2]
            three_back = 0 if i-3 < 0 else dp[i-3]
            dp[i] = max(two_back, three_back)+nums[i]
        for i in range(1, n):
            two_back = 0 if i-2 < 0 else dp2[i-2]
            three_back = 0 if i-3 < 0 else dp2[i-3]
            dp2[i] = max(two_back, three_back)+nums[i]
        return max(max(dp), max(dp2))
