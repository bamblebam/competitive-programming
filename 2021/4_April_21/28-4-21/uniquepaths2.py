class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] != 0:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[0][i] != 0:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
        for i in range(1, n):
            if obstacleGrid[i][0] != 0:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 0:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + \
                        obstacleGrid[i-1][j]
        return obstacleGrid[n-1][m-1]
