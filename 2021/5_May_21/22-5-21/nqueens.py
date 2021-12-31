class Solution:
    def solveNQueens(self, n: int):
        ans = list()

        def format_board(state):
            board = list()
            for row in state:
                board.append("".join(row))
            return board

        def solve(row, cols, diag, antidiag, state):
            if row == n:
                ans.append(format_board(state))
                return
            for col in range(n):
                currdiag = row-col
                currantidiag = row+col
                if col in cols or currantidiag in antidiag or currdiag in diag:
                    continue
                cols.add(col)
                antidiag.add(currantidiag)
                diag.add(currdiag)
                state[row][col] = 'Q'
                solve(row+1, cols, diag, antidiag, state)
                cols.remove(col)
                antidiag.remove(currantidiag)
                diag.remove(currdiag)
                state[row][col] = '.'
        empty = [['.']*n for _ in range(n)]
        solve(0, set(), set(), set(), empty)
        return ans
