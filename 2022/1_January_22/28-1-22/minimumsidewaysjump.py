class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        #each entry in dp is the lane
        #when we find an obstacle we make that lane infinite and go to the other 2 lanes using a jump
        #we keep this count and take the min
        dp=[1,0,1]
        for lane in obstacles:
            if lane:
                dp[lane-1]=float("inf")
            for i in range(3):
                if lane!=i+1:
                    dp[i]=min(dp[i],dp[(i+1)%3]+1,dp[(i+2)%3]+1)
        return min(dp)