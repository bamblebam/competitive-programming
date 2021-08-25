class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = math.isqrt(c)
        num_set = set()
        for i in range(limit+1):
            if c-i**2 in num_set:
                return True
            if i**2 == c/2:
                return True
            num_set.add(i**2)
        return False
