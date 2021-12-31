class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #use dfs
        #put all 2s in the queue then check adjacent cells, if 1 convert them to 2 and put them in new queue.
        #when curr queue is empty replace it with new queue.
        #check if all oranges are rotten or not and then return the answer.
        m=len(grid)
        n=len(grid[0])
        curr=deque()
        new=deque()
        num_oranges=0
        num_rotten=0
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        time=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    num_oranges+=1
                elif grid[i][j]==2:
                    num_oranges+=1
                    num_rotten+=1
                    curr.append((i,j))
                    
        while curr:
            x,y = curr.popleft()
            for dx,dy in dirs:
                nx,ny=dx+x,dy+y
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    grid[nx][ny]=2
                    num_rotten+=1
                    new.append((nx,ny))
            if not curr:
                time+=1
                curr=new
                new=deque()
                
        if num_oranges==0:
            return 0
        if num_rotten!=num_oranges:
            return -1
        return time-1
            