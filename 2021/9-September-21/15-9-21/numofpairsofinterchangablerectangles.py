class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans_map=defaultdict(lambda:0)
        for x,y in rectangles:
            ans_map[x/y]+=1
        ans=0
        for v in ans_map.values():
            if v!=1:
                ans+=((v-1)**2+(v-1))//2
        return ans