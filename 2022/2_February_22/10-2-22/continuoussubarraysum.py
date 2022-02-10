class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen=dict()
        seen[0]=-1
        curr=0
        for i,num in enumerate(nums):
            curr=(curr+num)%abs(k) if k else curr+a
            if i-seen.setdefault(curr,i)>1:
                return True
        return False