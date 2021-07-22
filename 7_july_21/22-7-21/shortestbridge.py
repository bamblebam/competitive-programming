class Solution:
    def shortestBridge(self, grid) -> int:
        n=len(grid)
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        def first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]==1:
                        return i,j
        boundaries=list()
        def dfs(i,j):
            grid[i][j]=-1 
            for dx,dy in dirs:
                x=i+dx
                y=j+dy
                if 0<=x<n and 0<=y<n and grid[x][y]!=-1:
                    if grid[x][y]==0:
                        boundaries.append((x,y))
                    else:
                        dfs(x,y)
                        
        dfs(*first())
        steps=1
        while boundaries:
            new=list()
            for i,j in boundaries:
                for dx,dy in dirs:
                    x=i+dx
                    y=j+dy
                    if 0<=x<n and 0<=y<n and grid[x][y]!=-1:
                        if grid[x][y]==1:
                            return steps
                        else:
                            grid[x][y]=-1
                            new.append((x,y))
            boundaries=new
            steps+=1
            
                            
        