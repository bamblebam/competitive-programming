class Solution:
    def numFactoredBinaryTrees(self, arr):
        answer = 0
        arr.sort()
        dp = dict()
        for i in arr:
            curr_ans = 1
            limit = i**0.5
            for j in arr:
                if j > limit:
                    break
                if not i % j and i//j in dp:
                    curr_ans += 2*dp[j] * \
                        dp[i//j] if j != i//j else dp[j]*dp[i//j]
            dp[i] = curr_ans
            answer += curr_ans
        return answer % (10**9+7)
