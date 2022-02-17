class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=list()
        n=len(candidates)
        def helper(target,curr,k):
            if target==0:
                ans.append(curr)
            if target<0 or k>=n:
                return
            for i in range(k,n):
                helper(target-candidates[i],curr+[candidates[i]],i)
        
        helper(target,[],0)
        return ans
                