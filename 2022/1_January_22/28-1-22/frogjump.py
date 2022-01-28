class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n=len(stones)
        stoneSet=set(stones)
        @lru_cache(None)
        def helper(idx,k):
            # print(idx,k)
            if idx>stones[-1] or k==0:
                return False
            if idx==stones[-1]:
                return True
            if idx+k not in stoneSet:
                return False
            else:
                return helper(idx+k,k) or helper(idx+k,k-1) or helper(idx+k,k+1)
            return False
        return helper(0,1)