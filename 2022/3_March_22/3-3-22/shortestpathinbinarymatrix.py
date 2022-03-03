class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        n=len(grid)
        if grid[0][0]==1:
            return -1
        queue=deque([(0,0,1)])
        seen=set((0,0))
        while queue:
            x,y,steps=queue.popleft()
            if x==y==n-1:
                return steps
            for dx,dy in dirs:
                nx=x+dx
                ny=y+dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in seen and grid[nx][ny]==0:
                    queue.append((nx,ny,steps+1))
                    seen.add((nx,ny))
        return -1