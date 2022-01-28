class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        rows=Counter()
        cols=Counter()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (rows[i]>1 or cols[j]>1):
                    ans+=1
        
        return ans