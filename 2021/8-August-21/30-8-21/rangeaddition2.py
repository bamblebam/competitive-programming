class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        # multiply the minimum x with the minimum y coordinate to get the range that is the most overlapped
        return min(i for i, _ in ops+[[m, n]])*min(j for _, j in ops+[[m, n]])
