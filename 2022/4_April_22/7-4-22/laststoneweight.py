class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=list()
        for x in stones:
            heappush(h,-x)
        
        while len(h)>1:
            x=-heappop(h)
            y=-heappop(h)
            if x==y:
                continue
            heappush(h,-(x-y))
        
        return -h[0] if h else 0