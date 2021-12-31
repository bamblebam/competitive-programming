from collections import Counter


class Solution:
    def canReorderDoubled(self, arr) -> bool:
        c = Counter(arr)
        for x in sorted(c, key=abs):
            if c[x] > c[x*2]:
                return False
            c[x*2] -= c[x]
        return True
