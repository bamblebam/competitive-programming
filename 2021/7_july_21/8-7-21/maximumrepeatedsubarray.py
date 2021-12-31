class Solution:
    def findLength(self, nums1, nums2) -> int:
        n=len(nums1)
        m=len(nums2)
        ans=0
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    ans=max(ans,dp[i][j])
        return ans
        