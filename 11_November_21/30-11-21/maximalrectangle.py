class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #based on largest rectangle in histogram problem
        #TC=O(mn)
        #put all the continuous row heights in the row array for each row
        #then in the hist function we go over all these heights and multiply it with the width
        
        def hist(heights):
            ans,stack=0,list()
            for i,h in enumerate(heights + [0]):
                while stack and heights[stack[-1]]>=h:
                    new_h=heights[stack.pop()]
                    w=i if not stack else i-stack[-1]-1
                    ans=max(ans,w*new_h)
                stack.append(i)
            return ans
        
        if not matrix or not matrix[0]:
            return 0
        m,n=len(matrix),len(matrix[0])
        ans=0
        
        row=[0]*n
        
        for i in range(m):
            for j in range(n):
                row[j]=0 if matrix[i][j]=="0" else row[j]+1
            ans=max(ans,hist(row))
        
        return ans
        