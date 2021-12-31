import itertools


class Solution:
    def ambiguousCoordinates(self, s: str):
        def make(segment):
            n = len(segment)
            for i in range(1, n+1):
                left, right = segment[:i], segment[i:]
                if(not left.startswith('0') or left == '0') and (not right.endswith('0')):
                    yield left+('.' if i != n else '')+right
        s = s[1:-1]
        return["({}, {})".format(*pair) for i in range(1, len(s)) for pair in itertools.product(make(s[:i]), make(s[i:]))]
