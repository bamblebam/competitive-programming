from sortedcontainers import SortedList

class CountIntervals:
    """
    use merge intervals logic to merge the intervals in a stream
    in normal merge intervals we just sort all the intervals and add them but we cant do that here since data is in a stream
    so we find idx where the interval should be inserted
    we check for all intervals that start after it and check if their start is less than our intervals end if yes we merge them
    we check if the interval before us has an end which is greater than our start and merge it as well
    also keep track of how many elements we are displacing
    """

    def __init__(self):
        self.cnt=0
        self.intervals=SortedList()

    def add(self, left: int, right: int) -> None:
        k=self.intervals.bisect_left((left,right))
        while k<len(self.intervals) and self.intervals[k][0]<=right:
            l,r=self.intervals.pop(k)
            self.cnt-=r-l+1
            right=max(r,right)
        if k and self.intervals[k-1][1]>=left:
            l,r=self.intervals.pop(k-1)
            self.cnt-=r-l+1
            left=l
            right=max(right,r)
        self.cnt+=right-left+1
        self.intervals.add((left,right))

    def count(self) -> int:
        return self.cnt
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()