import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        x_limit = bound if x == 1 else int(math.log(bound, x))
        y_limit = bound if y == 1 else int(math.log(bound, y))
        answer = set()
        for i in range(x_limit+1):
            for j in range(y_limit+1):
                value = x**i+y**j
                if value <= bound:
                    answer.add(value)
                if y == 1:
                    break
            if x == 1:
                break
        return list(answer)
