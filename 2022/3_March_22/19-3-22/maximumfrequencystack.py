class FreqStack:

    def __init__(self):
        self.count=Counter()
        self.groups=defaultdict(list)
        self.max=0

    def push(self, val: int) -> None:
        self.count[val]+=1
        self.max=max(self.max,self.count[val])
        self.groups[self.count[val]].append(val)

    def pop(self) -> int:
        x=self.groups[self.max].pop()
        self.count[x]-=1
        if not self.groups[self.max]:
            self.max-=1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()