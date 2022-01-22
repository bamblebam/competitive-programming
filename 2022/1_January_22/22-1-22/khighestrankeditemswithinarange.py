class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        seen=set()
        ans=list()
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        queue=deque([(start[0],start[1],0)])
        m,n=len(grid),len(grid[0])
        low,high=pricing
        seen.add((start[0],start[1]))
        
        if grid[start[0]][start[1]]==0:
            return 0
        
        while queue:
            x,y,steps=queue.popleft()
            # print(x,y,steps,grid[x][y])
            if low<=grid[x][y]<=high:
                ans.append((steps,grid[x][y],x,y))
            for dx,dy in dirs:
                nx=x+dx
                ny=y+dy
                # print(nx,ny)
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen and grid[x][y]!=0:
                    queue.append((nx,ny,steps+1))
                    seen.add((nx,ny))
        
        ans.sort()
        res=list()
        for i in range(min(k,len(ans))):
            res.append((ans[i][2],ans[i][3]))
        
        return res