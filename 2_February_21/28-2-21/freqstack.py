from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.stack = defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        f = self.freq[x]+1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.stack[f].append(x)

    def pop(self) -> int:
        x = self.stack[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.stack[self.maxfreq]:
            self.maxfreq -= 1
        return x

        # Your FreqStack object will be instantiated and called as such:
        # obj = FreqStack()
        # obj.push(x)
        # param_2 = obj.pop()
