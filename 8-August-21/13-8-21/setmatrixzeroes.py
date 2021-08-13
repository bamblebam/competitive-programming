class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for x in range(rows):
                        if matrix[x][j] != 0:
                            matrix[x][j] = 'a'
                    for x in range(cols):
                        if matrix[i][x] != 0:
                            matrix[i][x] = 'a'
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
