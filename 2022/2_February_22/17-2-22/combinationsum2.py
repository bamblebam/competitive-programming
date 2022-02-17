class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #to avoid duplicates just sort and check if prev not same
        ans=list()
        n=len(candidates)
        candidates.sort()
        def helper(target,curr,k):
            if target==0:
                ans.append(curr)
            if target<0 or k>=n:
                return
            for i in range(k,n):
                if i>k and candidates[i]==candidates[i-1]:
                    continue
                helper(target-candidates[i],curr+[candidates[i]],i+1)
        helper(target,[],0)
        return ans