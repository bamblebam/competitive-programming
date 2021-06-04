class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        div = 1e9 + 7
        n1, n2 = len(horizontalCuts), len(verticalCuts)
        horizontalCuts.sort()
        verticalCuts.sort()
        mh, mv = max(h-horizontalCuts[-1], horizontalCuts[0]
                     ), max(w-verticalCuts[-1], verticalCuts[0])
        for i in range(1, n1):
            mh = max(mh, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, n2):
            mv = max(mv, verticalCuts[i]-verticalCuts[i-1])
        return int(mh*mv % div)
