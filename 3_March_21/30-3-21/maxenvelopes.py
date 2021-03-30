import bisect


class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = list()
        for width, height in envelopes:
            point = bisect.bisect_left(dp, height)
            if point == len(dp):
                dp.append(height)
            else:
                dp[point] = height
        return len(dp)
