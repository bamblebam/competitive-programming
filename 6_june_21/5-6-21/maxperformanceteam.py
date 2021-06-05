import heapq


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        ans, total = 0, 0
        h = []
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            total += s
            heapq.heappush(h, s)
            while len(h) > k:
                total -= heapq.heappop(h)
            ans = max(ans, e*total)
        return int(ans % (10**9 + 7))
