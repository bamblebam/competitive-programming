class Solution:
    """
    use binary search to find out the maximum diff in heights
    do bfs on the grid and check if there is a path with abs diff less than or equal to target
    if yes then reduce right and check for even smaller target
    else increase left and search for bigger target
    """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n=len(heights),len(heights[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        
        if m==n==1:
            return 0
        
        def bfs(target):
            queue=deque([(0,0)])
            seen={(0,0)}

            while queue:
                x,y=queue.popleft()

                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen and abs(heights[x][y]-heights[nx][ny])<=target:
                        seen.add((nx,ny))
                        queue.append((nx,ny))
                        if nx==m-1 and ny==n-1:
                            return True
            return False
        
        l,r=0,10**6
        while l<r:
            mid=(l+r)//2
            if bfs(mid):
                r=mid
            else:
                l=mid+1
        
        return l
            