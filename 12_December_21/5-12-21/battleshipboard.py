class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        #use dfs to mark all tiles as 0 if a battlesghip has been found
        #iterate through all the tiles if it is X use dfs. It will automatically turn all connected tiles to 0
        count=0
        m,n=len(board),len(board[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(x,y):
            board[x][y]=0
            for dx,dy in dirs:
                nx=x+dx
                ny=y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=="X":
                    dfs(nx,ny)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="X":
                    dfs(i,j)
                    count+=1
        
        return count