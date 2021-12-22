class RangeFreqQuery:
    #use binary search for this
    #store all indices of each element in defaultdict
    #then use bisect to get the number of indices of that particular value for the range left and right

    def __init__(self, arr: List[int]):
        self.lookup=defaultdict(list)
        for i,x in enumerate(arr):
            self.lookup[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        l=bisect.bisect_left(self.lookup[value],left)
        if l>=len(self.lookup[value]):
            return 0
        r=bisect.bisect_right(self.lookup[value],right)-1
        if r>=len(self.lookup[value]):
            return len(self.lookup[value])-l
        return r-l+1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)