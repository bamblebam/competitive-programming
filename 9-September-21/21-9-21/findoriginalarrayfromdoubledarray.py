class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = OrderedDict(sorted(Counter(changed).items(), reverse=True))
        ans = list()
        seen = set()
        if changed.count(0) % 2:
            return list()
        for k, v in count.items():
            c = k/2
            if c in count:
                t = min(v, count[c])
                if c == k:
                    t = int(t/2)
                count[c] -= t
                count[k] -= t
                for i in range(t):
                    ans.append(c)
            if count[k] <= 0:
                seen.add(k)
        ans = list(map(int, ans))
        if len(seen) == len(set(changed)):
            return ans
        return list()
