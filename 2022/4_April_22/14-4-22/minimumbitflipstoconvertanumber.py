class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n=32
        ans=0
        for i in range(n):
            if start&1<<i!=goal&1<<i:
                ans+=1
        return ans