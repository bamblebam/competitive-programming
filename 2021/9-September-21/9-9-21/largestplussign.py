class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[0]*n for _ in range(n)]
        ans = 0
        mines = [(x, y) for x, y in mines]
        # for rows
        for i in range(n):
            count = 0
            for j in range(n):
                if (i, j) not in mines:
                    count += 1
                    dp[i][j] = count
                else:
                    count = 0
            count = 0
            for j in range(n-1, -1, -1):
                if (i, j) not in mines:
                    count += 1
                    dp[i][j] = min(count, dp[i][j])
                else:
                    count = 0
        # for cols
        for j in range(n):
            count = 0
            for i in range(n):
                if (i, j) not in mines:
                    count += 1
                    dp[i][j] = min(count, dp[i][j])
                else:
                    count = 0
            count = 0
            for i in range(n-1, -1, -1):
                if (i, j) not in mines:
                    count += 1
                    dp[i][j] = min(count, dp[i][j])
                else:
                    count = 0
                ans = max(ans, dp[i][j])

        return ans
