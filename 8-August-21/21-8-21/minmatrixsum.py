class Solution:
    def maxMatrixSum(self, matrix) -> int:
        h = list()
        n = len(matrix)
        neg = 0
        for i in range(n):
            for j in range(n):
                h.append(abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    neg += 1
        sum_ = sum(h)
        if not neg % 2:
            return sum_
        return sum_ - sorted(h)[0]*2
