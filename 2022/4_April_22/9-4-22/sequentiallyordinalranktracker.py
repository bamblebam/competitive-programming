from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.h=SortedList()
        self.rank=-1

    def add(self, name: str, score: int) -> None:
        self.h.add((-score,name))

    def get(self) -> str:
        self.rank+=1
        return self.h[self.rank][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()