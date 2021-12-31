class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def check(s, t):
            t = iter(t)
            return all(c in t for c in s)

        possible = "".join(el*(freq//k) for el, freq in Counter(s).items())
        combs = set()
        for i in range(len(possible)+1):
            for cand in combinations(possible, i):
                for perm in permutations(cand):
                    combs.add("".join(perm))
        combs = sorted(combs, key=lambda x: (len(x), x), reverse=True)
        for c in combs:
            if check(c*k, s):
                return c
