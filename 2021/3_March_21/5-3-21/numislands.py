class Solution:
    def helper(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return None
        grid[i][j] = '0'
        self.helper(grid, i-1, j)
        self.helper(grid, i+1, j)
        self.helper(grid, i, j-1)
        self.helper(grid, i, j+1)

    def numIslands(self, grid) -> int:
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    answer += 1
                    self.helper(grid, i, j)
        return answer
    
    #alternative solution
    # class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     #ans is for size of largest island
    #     #do dfs on each island and add the count to parent func. via recursion you will get size of island
    #     #num_island is for number of islands
    #     m,n=len(grid),len(grid[0])
    #     ans=0
    #     num_islands=0
    #     dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    #     def dfs(x,y):
    #         count=1
    #         grid[x][y]=0
    #         for dx,dy in dirs:
    #             nx,ny=x+dx,y+dy
    #             if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1':
    #                 count+=dfs(nx,ny)
    #         return count
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]=="1":
    #                 ans=max(ans,dfs(i,j))
    #                 num_islands+=1
    #     return num_islands
