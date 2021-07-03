from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prefix = [[0]*(cols+1) for _ in range(rows+1)]
        ans = -float('inf')

        for x in range(rows):
            for y in range(cols):
                prefix[x+1][y+1] += prefix[x+1][y]+matrix[x][y]
        for x in range(rows):
            for y in range(cols):
                prefix[x+1][y+1] += prefix[x][y+1]

        for x1 in range(rows):
            for x2 in range(x1, rows):
                s = SortedList()
                s.add(0)
                for y in range(cols):
                    curr = prefix[x2+1][y+1]-prefix[x1][y+1]
                    target = curr-k
                    idx = s.bisect_left(target)
                    if 0 <= idx < len(s):
                        ans = max(ans, curr-s[idx])
                    s.add(curr)
        return ans
