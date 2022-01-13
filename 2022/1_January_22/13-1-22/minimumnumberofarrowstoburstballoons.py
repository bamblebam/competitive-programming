class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #we sort it on the basis of end
        #if the curr end is smaller than the next start it does'nt overlap and count needs to be increnebted and curr end needs to be updated
        points.sort(key=lambda x:x[1])
        n=len(points)
        curr=points[0]
        count=1
        for i in range(n):
            if curr[1]<points[i][0]:
                count+=1
                curr=points[i]
        return count