class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        ans=0
        for num,v in count.items():
            if v==0:
                continue
            target=k-num
            if target<=0:
                continue
            elif target==num:
                x=v//2
                ans+=x
                count[target]-=x
                continue
            new_v=count[target]
            if new_v==0:
                continue
            x=min(v,new_v)
            count[num]-=x
            count[target]-=x
            ans+=x
        return ans