class Solution:

    def pacificAtlantic(self, matrix):
        if len(matrix) == 0:
            return []
        pacific = set()
        atlantic = set()

        def helper(row, col, reachable):
            reachable.add((row, col))
            for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row = row+x
                new_col = col+y
                if new_row < 0 or new_col < 0 or new_row >= len(matrix) or new_col >= len(matrix[0]):
                    continue
                elif matrix[new_row][new_col] < matrix[row][col]:
                    continue
                elif (new_row, new_col) in reachable:
                    continue
                helper(new_row, new_col, reachable)
        for i in range(len(matrix)):
            helper(i, 0, pacific)
            helper(i, len(matrix[0])-1, atlantic)
        for i in range(len(matrix[0])):
            helper(0, i, pacific)
            helper(len(matrix)-1, i, atlantic)
        return list(pacific.intersection(atlantic))


sol = Solution()
print(sol.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
