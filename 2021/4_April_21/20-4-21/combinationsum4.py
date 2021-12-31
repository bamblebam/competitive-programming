class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [1]+[0]*target
        for i in range(target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]
