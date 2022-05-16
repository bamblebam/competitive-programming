class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        ans=0
        last=bottom-1
        special.sort()
        for floor in special+[top+1]:
            ans=max(floor-last-1,ans)
            last=floor
        return ans