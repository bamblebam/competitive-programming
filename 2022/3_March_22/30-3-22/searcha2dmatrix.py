class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=list()
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            rows.append(matrix[i][-1])
        
        idx=bisect_left(rows,target)
        
        if idx==m:
            return False
        
        row=matrix[idx]
        l,r=0,n-1
        
        while l<=r:
            mid=(l+r)//2
            if row[mid]==target:
                return True
            elif row[mid]<target:
                l=mid+1
            else:
                r=mid-1
        
        return False
                