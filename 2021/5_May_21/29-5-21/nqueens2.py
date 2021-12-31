class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0

        def solve(row, cols, diag, antidiag, state):
            if row == n:
                self.ans += 1
                return
            for col in range(n):
                currdiag = row-col
                currantidiag = row+col
                if col in cols or currdiag in diag or currantidiag in antidiag:
                    continue
                cols.add(col)
                diag.add(currdiag)
                antidiag.add(currantidiag)
                state[row][col] = 1
                solve(row+1, cols, diag, antidiag, state)
                cols.remove(col)
                diag.remove(currdiag)
                antidiag.remove(currantidiag)
                state[row][col] = 0
        board = [[0]*n for _ in range(n)]
        solve(0, set(), set(), set(), board)
        return self.ans
