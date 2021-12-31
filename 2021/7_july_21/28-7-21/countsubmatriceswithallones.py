class Solution:
    def numSubmat(self, mat) -> int:
        rows=len(mat)
        cols=len(mat[0])
        ans=0
        
        for i in range(rows):
            for j in range(cols):
                if i>0 and mat[i][j]!=0:
                    mat[i][j]+=mat[i-1][j]
        
        for i in range(rows):
            stack=list()
            count=0
            for j in range(cols):
                while stack and mat[i][stack[-1]]>mat[i][j]:
                    start=stack.pop()
                    end=stack[-1] if stack else -1
                    count-=(mat[i][start]-mat[i][j])*(start-end)
                count+=mat[i][j]
                ans+=count
                stack.append(j)
        
        return ans