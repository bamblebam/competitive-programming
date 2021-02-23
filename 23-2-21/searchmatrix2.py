class Solution:
    def searchMatrix(self, matrix, target):
        m = 0
        n = len(matrix[0])-1
        while(m < len(matrix) and n >= 0):
            if matrix[m][n] > target:
                n -= 1
            elif matrix[m][n] < target:
                m += 1
            else:
                return True
        else:
            return False


sol = Solution()
print(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
      3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target=20))
