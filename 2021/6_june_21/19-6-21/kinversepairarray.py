class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        mod = 10**9+7
        for i in range(1, n+1):
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i-1][j]+mod-(dp[i-1][j-i]
                           if j-i >= 0 else 0)) % mod
                    dp[i][j] = (dp[i][j-1]+val) % mod
        return (dp[n][k]+mod-(dp[n][k-1] if k > 0 else 0)) % mod

# alternate solution
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         mod=10**9+7
#         dp=[[1]*(k+1) for _ in range(n+1)]
#         sp=[[1]*(k+1) for _ in range(n+1)]
#         for i in range(1,n+1):
#             for j in range(1,k+1):
#                 dp[i][j]=sp[i-1][j] if j<i else (sp[i-1][j]-sp[i-1][j-i])%mod
#                 sp[i][j]=(sp[i][j-1]+dp[i][j])%mod
#         return dp[-1][-1]
