class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9+7
        if n == 1:
            return 5
        pdp = [1]*5
        dp = [0]*5
        for i in range(2, n+1):
            dp = [0]*5
            dp[0] = (pdp[1]+pdp[2]+pdp[4]) % mod
            dp[1] = (pdp[0]+pdp[2]) % mod
            dp[2] = (pdp[1]+pdp[3]) % mod
            dp[3] = (pdp[2]) % mod
            dp[4] = (pdp[2]+pdp[3]) % mod
            pdp = dp
        return sum(dp) % mod
