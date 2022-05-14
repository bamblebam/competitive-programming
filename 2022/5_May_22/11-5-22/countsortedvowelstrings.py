class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans=0
        cands=['a','e','i','o','u']
        
        def helper(path,idx):
            nonlocal ans
            if len(path)==n:
                ans+=1
                return
            for i in range(idx,5):
                helper(path+[cands[i]],i)
        
        helper([],0)
        return ans