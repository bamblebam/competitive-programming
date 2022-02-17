class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=list()
        def helper(curr,idx,k):
            if k==0:
                ans.append(curr)
            if k<0 or idx>n:
                return
            for i in range(idx,n+1):
                helper(curr+[i],i+1,k-1)
        helper([],1,k)
        return ans