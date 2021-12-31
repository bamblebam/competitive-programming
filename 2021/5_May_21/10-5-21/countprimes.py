import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        numbers = set()
        for i in range(2, int(math.sqrt(n))+1):
            if i not in numbers:
                for j in range(i*i, n, i):
                    numbers.add(j)
        return n-2-len(numbers)
