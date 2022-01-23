class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[x for x in nums if x>0]
        neg=[x for x in nums if x<0]
        ans=list()
        for p,n in zip(pos,neg):
            ans.append(p)
            ans.append(n)
        return ans