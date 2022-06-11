class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016199/Python-O(n)-solution-using-cumulative-sums
        """
        ans=-float('inf')
        prefix=[0]+list(accumulate(nums))
        indices={c:i for i,c in enumerate(prefix)}
        goal=prefix[-1]-x
        
        if goal<0: return -1
        
        for num in indices:
            if num+goal in indices:
                ans=max(ans,indices[num+goal]-indices[num])
        
        return len(nums) - ans if ans!=-float('inf') else -1