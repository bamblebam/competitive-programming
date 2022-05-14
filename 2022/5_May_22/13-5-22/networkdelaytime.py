class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[0]+[float('inf')]*n
        
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        h=[(0,k)]
        
        while h:
            time,node=heappop(h)
            if dist[node]>time:
                dist[node]=time
                for v,w in graph[node]:
                    heappush(h,(w+time,v))
        
        ans=max(dist)
        return ans if ans!=float('inf') else -1