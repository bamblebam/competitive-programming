class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
        sort intervals on the basis of smaleest left and largest right
        this way you can just keep track of largest right and if you find an interval with smaller right it can be merged
        because if the left is same the right will be smaller and if the left is bigger than the rights left and the right is smaller then also it is in interval
        rem is the amount of intervals merged so n0rem is the ones left
        '''
        intervals.sort(key=lambda x:(x[0],-x[1]))
        right,rem=0,0
        n=len(intervals)
        for l,r in intervals:
            if r<=right:
                rem+=1
            else:
                right=r
        return n-rem
        