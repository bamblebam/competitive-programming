from collections import defaultdict


class Solution:
    def maximumGap(self, nums) -> int:
        h, l, n = max(nums), min(nums), len(nums)
        if n <= 2 or h == l:
            return h-l
        d = defaultdict(list)
        for i in nums:
            idx = n-2 if i == h else (i-l)*(n-1)//(h-l)
            d[idx].append(i)
        cands = [[min(d[x]), max(d[x])] for x in range(n-1) if d[x]]
        return max(y[0]-x[1] for x, y in zip(cands, cands[1:]))
