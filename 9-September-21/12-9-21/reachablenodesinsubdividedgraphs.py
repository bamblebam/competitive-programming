class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        #creating a graph
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        h=[(0,0)]
        dist=[float('inf')]*n
        dist[0]=0
        
        #djikstras algorithm
        while h:
            d,node=heapq.heappop(h)
            if d>dist[node]:
                continue
            for v,w in graph[node]:
                if dist[v]>d+w+1:
                    dist[v]=d+w+1
                    heapq.heappush(h,(d+w+1,v))
        
        ans=0
        for i in range(n):
            if maxMoves>=dist[i]:
                ans+=1
        for u,v,w in edges:
            left=max(maxMoves-dist[u],0)
            right=max(maxMoves-dist[v],0)
            ans+=min(left+right,w)
        
        return ans