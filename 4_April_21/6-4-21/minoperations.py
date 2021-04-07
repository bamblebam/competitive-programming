class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2:
            return sum([i for i in range(0, n, 2)])
        else:
            return int((n/2)**2)
