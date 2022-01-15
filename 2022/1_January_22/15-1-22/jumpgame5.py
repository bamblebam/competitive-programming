class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        #use recursion
        #go through each pillar and check all the pillars in range d that are smaller than it and meet the other conditions
        #then use recursion on them too and get the max num of pillars you can visit
        n=len(arr)
        
        @lru_cache(None)
        def helper(idx):
            result=1
            for i in range(idx-1,max(-1,idx-d-1),-1):
                if arr[idx]<=arr[i]:
                    break
                result=max(result,1+helper(i))
            for i in range(idx+1,min(n,idx+d+1)):
                if arr[idx]<=arr[i]:
                    break
                result=max(result,1+helper(i))
            return result
        
        ans=0
        for i in range(n):
            ans=max(ans,helper(i))
        
        return ans
                