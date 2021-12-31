class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1]+[0]*(len(nums)-1)
        for i in range(len(nums)):
            max_ = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_ = max(max_, dp[j])
            dp[i] = max_+1
        return max(dp)


sol = Solution()
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
