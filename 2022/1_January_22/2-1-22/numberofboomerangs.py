class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n=len(points)
        ans=0
        for i in range(n):
            x,y=points[i]
            count=Counter()
            for j in range(n):
                if i==j:
                    continue
                distance=(x-points[j][0])**2+(y-points[j][1])**2
                count[distance]+=1
            for v in count.values():
                if v>1:
                    ans+=2*comb(v,2)
        return ans