class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        ans = 0
        combs = list()
        for i in range(1, n+1):
            combs.extend(list(combinations(arr, i)))
        for cand in combs:
            t = "".join(cand)
            if len(set(t)) == len(t):
                ans = max(ans, len(t))
        return ans
