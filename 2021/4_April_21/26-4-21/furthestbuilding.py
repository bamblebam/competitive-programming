import heapq


class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        INF = float('inf')
        heights = [INF]+heights
        n = len(heights)
        h = list()
        for i in range(1, n):
            if heights[i] <= heights[i-1]:
                continue
            diff = heights[i]-heights[i-1]
            heapq.heappush(h, diff)
            while len(h) > ladders:
                bricks -= h[0]
                heapq.heappop(h)
            if bricks < 0:
                return i-2
        return n-2
