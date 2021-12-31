class DetectSquares:

    def __init__(self):
        self.points = Counter()
        self.xs = defaultdict(set)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.xs[point[0]].add(point[1])

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for py in self.xs[x]:
            diff = abs(py-y)
            if diff == 0:
                continue
            for px in [x+diff, x-diff]:
                if (px, py) in self.points and (px, y) in self.points and (x, py) in self.points:
                    count += self.points[(px, py)] * \
                        self.points[(px, y)]*self.points[(x, py)]
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
