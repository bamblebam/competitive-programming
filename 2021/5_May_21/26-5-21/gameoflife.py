class Solution:
    def gameOfLife(self, board) -> None:
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]
        n = len(board)
        m = len(board[0])

        def dfs(row, col):
            neighbors = 0
            for di in range(8):
                x = dx[di]+row
                y = dy[di]+col
                if x >= 0 and x < n and y >= 0 and y < m and board[x][y] > 0:
                    neighbors += 1
            if neighbors == 3 and board[row][col] == 0:
                board[row][col] = -1
            elif (neighbors < 2 or neighbors > 3) and board[row][col] == 1:
                board[row][col] = 2

        for i in range(n):
            for j in range(m):
                dfs(i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
