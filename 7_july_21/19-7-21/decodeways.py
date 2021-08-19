class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1]+[0]*n
        for i in range(n):
            # for 1 digit
            curr = s[i]
            if '1' <= curr <= '9':
                dp[i+1] += dp[i]
            # for 2 digit
            if i-1 >= 0:
                prev = s[i-1]
                if prev == '1':
                    dp[i+1] += dp[i-1]
                elif prev == '2':
                    if '0' <= curr <= '6':
                        dp[i+1] += dp[i-1]
        return dp[n]

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n=len(s)
#         dp=[1]+[0]*n
#         for i in range(n):
#             curr=s[i]
#             #for 1 digit
#             if '1'<=curr<='9':
#                 dp[i+1]+=dp[i]
#             #for 2 digit
#             if i-1>=0:
#                 prev=s[i-1]
#                 if prev=='1':
#                     dp[i+1]+=dp[i-1]
#                 elif prev=='2':
#                     if '0'<=curr<='6':
#                         dp[i+1]+=dp[i-1]
#         return dp[n]
        