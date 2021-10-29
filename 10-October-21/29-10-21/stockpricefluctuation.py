from sortedcontainers import SortedList

class StockPrice:
    #use sorted list for min and max queries in log(n) time
    def __init__(self):
        self.stock_map=defaultdict(lambda: 0)
        self.curr=(0,0)
        self.sl=SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if self.stock_map[timestamp]!=0:
            self.sl.remove(self.stock_map[timestamp])
        self.stock_map[timestamp]=price
        self.sl.add(price)
        if timestamp>=self.curr[0]:
            self.curr=(timestamp,price)

    def current(self) -> int:
        return self.curr[1]

    def maximum(self) -> int:
        return self.sl[-1]

    def minimum(self) -> int:
        return self.sl[0]
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()