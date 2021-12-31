class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        dp=[Counter() for num in nums]
        for i in range(n):
            for j in range(i):
                d=nums[i]-nums[j]
                dp[i][d]+=dp[j][d]+1
                ans+=dp[j][d]
        return ans