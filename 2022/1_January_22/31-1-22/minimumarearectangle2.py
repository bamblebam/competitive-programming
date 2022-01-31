class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        ans=float("inf")
        seen=defaultdict(list)
        for i,(x0,y0) in enumerate(points):
            for x1,y1 in points[i+1:]:
                cx=(x0+x1)/2
                cy=(y0+y1)/2
                d=(x0-x1)**2+(y0-y1)**2
                for xx,yy in seen[(cx,cy,d)]:
                    area=sqrt(((x0-xx)**2+(y0-yy)**2)*((y1-yy)**2+(x1-xx)**2))
                    ans=min(ans,area)
                seen[(cx,cy,d)].append((x0,y0))
        return ans if ans<float("inf") else 0