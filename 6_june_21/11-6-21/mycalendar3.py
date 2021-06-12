from bisect import bisect_left


class MyCalendarThree:

    def __init__(self):
        self.positions = list()
        self.count = dict()
        self.maxbooking = 0

    def book(self, start: int, end: int) -> int:
        pos = self.positions
        cnt = self.count
        i = bisect_left(pos, start)
        j = bisect_left(pos, end)
        if start not in cnt:
            startcnt = cnt[pos[i-1]] if i-1 >= 0 else 0
            pos.insert(i, start)
            j += 1
            cnt[start] = startcnt
        if end not in cnt:
            pos.insert(j, end)
            cnt[end] = cnt[pos[j-1]]
        for k in range(i, j):
            cnt[pos[k]] += 1
            self.maxbooking = max(self.maxbooking, cnt[pos[k]])
        return self.maxbooking


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
