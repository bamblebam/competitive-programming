class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        use dp to keep track whether a substring between i and j is palindromic or not
        """
        n=len(s)
        dp=[[0]*(n+1) for _ in range(n+1)]
        ans=0
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j]=s[i]==s[j] and (j-i+1<3 or dp[i+1][j-1])
                ans+=dp[i][j]
        
        return ans