class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        check how many times 101 and 010 are subsequences of string s
        """
        def helper(a,b):
            """
            returns the number of times second string is subsequence of first string
            """
            m,n=len(a),len(b)
            dp=[[0]*(n+1) for _ in range(m+1)]
            
            for i in range(n+1):
                dp[0][i]=0
            for i in range(m+1):
                dp[i][0]=1
            
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if a[i-1]==b[j-1]:
                        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j]
            
            return dp[m][n]
        
        return helper(s,'101')+helper(s,'010')
            