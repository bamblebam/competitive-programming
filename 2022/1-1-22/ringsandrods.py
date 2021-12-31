class Solution:
    def countPoints(self, rings: str) -> int:
        rod_map=defaultdict(set)
        for i in range(0,len(rings),2):
            rod_map[rings[i+1]].add(rings[i])
        ans=0
        for v in rod_map.values():
            if len(v)==3:
                ans+=1
        return ans