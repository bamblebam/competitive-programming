class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return list()
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False]*cols for _ in range(rows)]
        ans = list()
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(rows*cols):
            ans.append(matrix[r][c])
            visited[r][c] = True
            nr, nc = r+dr[di], c+dc[di]
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                r, c = nr, nc
            else:
                di = (di+1) % 4
                r, c = r+dr[di], c+dc[di]
        return ans
