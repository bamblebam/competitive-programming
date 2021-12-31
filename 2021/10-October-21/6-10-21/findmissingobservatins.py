class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        x = sum(rolls)
        missing_val = mean*(m+n)-x
        if missing_val > 6*n or missing_val < n:
            return list()
        a = missing_val//n
        b = missing_val % n
        ans = [a]*n
        for i in range(b):
            ans[i] += 1
        return ans
