class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        temp=list()
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                temp.append(matrix[i][j])
        temp.sort()
        return temp[k-1]