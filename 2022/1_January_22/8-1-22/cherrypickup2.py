class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #top down dp
        #dp row,col1,col2 is the max num of cherries that can be picked if the robots are in that position
        #can also use bottom up dp with 3d array
        m,n=len(grid),len(grid[0])
        @lru_cache(None)
        def dp(row,col1,col2):
            if not 0<=col1<n or not 0<=col2<n: #fail conds
                return float("-inf")
            #adding val of curr cell
            ans=0
            ans+=grid[row][col1]
            if col1!=col2:
                ans+=grid[row][col2]
            #transition into next cells .ie. the 3 cols that it can go to
            if row!=m-1:
                ans+=max(dp(row+1,ncol1,ncol2) for ncol1 in [col1,col1+1,col1-1] for ncol2 in [col2,col2+1,col2-1])
            return ans
        return dp(0,0,n-1)
        