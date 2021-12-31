class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        #use dfs and backtracking to solve the problem
        #TC is O(3^(m*n)) because we can go to 3 dirs in each step
        m,n=len(grid),len(grid[0])
        ans,empty=0,0 #empty is the number of empty cells
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(x,y,rem):
            #we use the rem variable to remember the number of empty cells remaining
            nonlocal ans
            if not 0<=x<m or not 0<=y<n or grid[x][y]<0: #invalid cell so return
                return
            if grid[x][y]==2 and rem==0: #reached final cell with all empty cells visited
                ans+=1
            for dx,dy in dirs:
                temp=grid[x][y]
                grid[x][y]=-2 #we mark cell as -2 to show that it is visited
                dfs(x+dx,y+dy,rem-1)
                grid[x][y]=temp
            
        for i,j in product(range(m),range(n)):
            if grid[i][j]==1:
                (sx,sy)=(i,j)
            empty+=(grid[i][j]!=-1)
        
        dfs(sx,sy,empty-1)
        return ans