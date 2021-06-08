class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            two_back = 0 if i-2 < 0 else dp[i-2]
            three_back = 0 if i-3 < 0 else dp[i-3]
            dp[i] = max(two_back, three_back)+nums[i]
        return max(dp)
