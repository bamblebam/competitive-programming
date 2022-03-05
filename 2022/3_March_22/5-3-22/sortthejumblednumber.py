class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n=len(nums)
        ans=list()
        def convert(num):
            num=str(num)
            final=""
            for x in num:
                final+=str(mapping[int(x)])
            return int(final)
        for i,num in enumerate(nums):
            ans.append((convert(num),i))
        ans.sort()
        res=list()
        for x,i in ans:
            res.append(nums[i])
        return res