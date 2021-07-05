class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        rows=len(mat)
        cols=len(mat[0])
        if rows*cols!=r*c:
            return mat
        ans=[[0]*c for _ in range(r)]
        temp=list()
        for i in range(rows):
            for j in range(cols):
                temp.append(mat[i][j])
        for i in range(r):
            for j in range(c):
                ans[i][j]=temp.pop(0)
        return ans
             
                