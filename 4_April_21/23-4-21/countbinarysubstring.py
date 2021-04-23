import itertools


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(group)) for key, group in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
