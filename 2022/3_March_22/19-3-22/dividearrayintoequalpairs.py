class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)
        count=Counter(nums)
        ans=0
        if n%2:
            return False
        for k,v in count.items():
            if v%2:
                return False
            ans+=v//2
        return ans==n//2