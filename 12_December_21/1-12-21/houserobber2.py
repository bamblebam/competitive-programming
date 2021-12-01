class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=3:
            return max(nums)
        def helper(nums):
            dp1,dp2=0,0
            for num in nums:
                dp1,dp2=dp2,max(dp2,dp1+num)
            return dp2
        return max(helper(nums[1:]),helper(nums[:-1]))