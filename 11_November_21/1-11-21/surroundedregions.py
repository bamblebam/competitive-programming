class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # use dfs on the O tiles near the border and hange all tiles connected to it to T
        # those are tiles which are not surrounded by water so they won't be converted to X
        # change the ones that are still O to X
        m=len(board)
        n=len(board[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i,j):
            board[i][j]='T'
            for dx,dy in dirs:
                nx=dx+i
                ny=dy+j
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                    dfs(nx,ny)
        
        for i in range(n):
            if board[0][i]=='O':
                dfs(0,i)
            if board[m-1][i]=='O':
                dfs(m-1,i)
        
        for j in range(m):
            if board[j][0]=='O':
                dfs(j,0)
            if board[j][n-1]=='O':
                dfs(j,n-1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'