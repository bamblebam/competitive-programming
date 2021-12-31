import heapq


class Solution:
    def isPossible(self, target) -> bool:
        h = [-i for i in target]
        heapq.heapify(h)
        sum_ = sum(target)
        if len(target) == 1:
            return target[0] == 1
        while sum_ > len(target):
            curr = -1*heapq.heappop(h)
            rest = sum_-curr
            if rest > curr:
                return False
            if rest == 1:
                return True
            prev = curr % rest
            if prev < 1:
                return False
            sum_ = rest+prev
            heapq.heappush(h, -prev)
        return True
