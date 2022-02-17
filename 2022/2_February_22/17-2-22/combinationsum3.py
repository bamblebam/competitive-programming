class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates=list(range(1,10))
        ans=list()
        l=len(candidates)
        def helper(target,curr,idx,k):
            if target==0 and k==0:
                ans.append(curr)
            if target<0 or k<0 or idx>=l:
                return
            for i in range(idx,l):
                helper(target-candidates[i],curr+[candidates[i]],i+1,k-1)
        helper(n,[],0,k)
        return ans