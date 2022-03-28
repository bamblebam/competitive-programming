class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m,n=len(mat),len(mat[0])
        ans=list()
        def helper(row,i):
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if row[mid]==0:
                    r=mid-1
                else:
                    l=mid+1
            ans.append((l,i))
        
        for i,row in enumerate(mat):
            helper(row,i)
        
        ans.sort()
        return [j for i,j in ans][:k]