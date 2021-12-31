class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=list()
        for i,(x,y) in enumerate(points):
            num=(x**2+y**2)
            ans.append((num,i))
        ans.sort()
        res=list()
        for i in range(k):
            res.append(points[ans[i][1]])
        return res
        