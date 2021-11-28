class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #use djikstras but keep a count array with it
        #if the distance from 0 to node for a particular instance is equal to the curr distance just add it to the curr distances count
        #if it is smaller replace the curr distance count with it
        #you add to the count because the new count will be the number of ways to reach the prior node + the number of ways we can reach curr node from it.
        mod=10**9 +7
        edges=defaultdict(list)
        for u,v,t in roads:
            edges[u].append((v,t))
            edges[v].append((u,t))
        
        dist=[float("inf")]*n
        dist[0]=0
        counts=[0]*n
        counts[0]=1
        h=[(0,0)]
        
        while h:
            d,u=heapq.heappop(h)
            if dist[u]<d:
                continue
            for v,t in edges[u]:
                if dist[u]+t==dist[v]:
                    counts[v]+=counts[u]
                    counts[v]%=mod
                elif dist[u]+t<dist[v]:
                    counts[v]=counts[u]
                    dist[v]=dist[u]+t
                    heapq.heappush(h,(dist[v],v))
        
        return counts[n-1]%mod
        
        