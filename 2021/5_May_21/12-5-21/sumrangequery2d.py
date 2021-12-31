class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sr, er = min(row1, row2), max(row1, row2)
        sc, ec = min(col1, col2), max(col1, col2)
        answer = 0
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                answer += self.matrix[i][j]
        return answer
