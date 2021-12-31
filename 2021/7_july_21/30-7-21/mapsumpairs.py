class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_map = dict()

    def insert(self, key: str, val: int) -> None:
        self.word_map[key] = val

    def sum(self, prefix: str) -> int:
        count = 0
        for k, v in self.word_map.items():
            if k.startswith(prefix):
                count += v
        return count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
