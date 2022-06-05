class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=1
        prev=None
        for num in nums:
            if prev==None:
                prev=num
                continue
            if num-prev>k:
                prev=num
                ans+=1
        return ans