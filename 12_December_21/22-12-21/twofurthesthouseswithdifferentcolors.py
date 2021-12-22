class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=1
        n=len(colors)
        for i in range(n):
            for j in range(i+1,n):
                if colors[i]!=colors[j]:
                    ans=max(ans,j-i)

        return ans