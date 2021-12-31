from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows=len(mat)
        cols=len(mat[0])
        ans=[[float('inf')]*cols for _ in range(rows)]
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
    
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i,j))
                    ans[i][j]=0
                
        while queue:
            x,y=queue.popleft()
            for dx,dy in dirs:
                nx,ny=dx+x,dy+y
                if not 0<=nx<rows or not 0<=ny<cols:
                    continue
                if ans[nx][ny]>ans[x][y]+1:
                    ans[nx][ny]=ans[x][y]+1
                    queue.append((nx,ny))
        
        return ans
                            
        
        