class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        """
        use recursion to keep track of the minimum score
        """
        m,n=len(grid),len(grid[0])
        
        @lru_cache(None)
        def helper(i,j):
            if i==m-1:
                return grid[i][j]
            return grid[i][j]+min(moveCost[grid[i][j]][k]+helper(i+1,k) for k in range(n))
        
        return min(helper(0,i) for i in range(n))