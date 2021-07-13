class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9+7
        n = len(s)
        dp = [1]+[0]*n
        for i in range(n):
            # for single digit
            curr = s[i]
            if '1' <= curr <= '9':
                dp[i+1] += dp[i]
            elif curr == '*':
                dp[i+1] += 9*dp[i]
            # for double digit
            if i-1 >= 0:
                prev = s[i-1]
                if prev == '1':
                    if '0' <= curr <= '9':
                        dp[i+1] += dp[i-1]
                    elif curr == '*':
                        dp[i+1] += 9*dp[i-1]
                elif prev == '2':
                    if '0' <= curr <= '6':
                        dp[i+1] += dp[i-1]
                    elif curr == '*':
                        dp[i+1] += 6*dp[i-1]
                elif prev == '*':
                    if '0' <= curr <= '9':
                        dp[i+1] += dp[i-1]
                    if '0' <= curr <= '6':
                        dp[i+1] += dp[i-1]
                    if curr == '*':
                        dp[i+1] += 15*dp[i-1]
            dp[i] %= mod
        return dp[n] % mod
