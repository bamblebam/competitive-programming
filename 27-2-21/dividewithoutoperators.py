import sys


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        j = 0
        divisor2, dividend2 = abs(divisor), abs(dividend)
        for i in range(32, -1, -1):
            if dividend2 >= divisor2 << i:
                dividend2 -= divisor2 << i
                j += 1 << i
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            j = -j
        return min(2**31-1, max(-2**31-1, j))


sol = Solution()
print(sol.divide(-8, -2))
