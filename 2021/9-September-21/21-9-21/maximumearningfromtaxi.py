# similar to 1235 job scheduling problem
# done by dp and greedy can also use line sweep

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        n_rides = len(rides)
        rides = sorted(rides)
        s = [ride[0] for ride in rides]
        dp = [0]*(n_rides+1)
        for i in range(n_rides-1, -1, -1):
            temp = bisect_left(s, rides[i][1])
            dp[i] = max(dp[i+1], dp[temp]+rides[i][1]-rides[i][0]+rides[i][2])
        return dp[0]
