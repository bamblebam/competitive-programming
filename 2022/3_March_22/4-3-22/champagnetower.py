class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        kkep track of how much water has passed through a glass
        use simulation
        """
        dp=[[0]*k for k in range(1,102)]
        dp[0][0]=poured
        for r in range(query_row+1):
            for c in range(r+1):
                x=(dp[r][c]-1)/2
                if x>0:
                    dp[r+1][c]+=x
                    dp[r+1][c+1]+=x
        return min(1,dp[query_row][query_glass])