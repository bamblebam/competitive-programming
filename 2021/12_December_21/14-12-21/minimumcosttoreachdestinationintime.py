class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        #use modified djikstras algorithm
        edges_map=defaultdict(set)
        n=len(passingFees)
        for u,v,t in edges:
            edges_map[u].add((v,t))
            edges_map[v].add((u,t))
        
        ans=float("inf")
        lowest=[float("inf")]*n #lowest cost at node x
        best=[[float("inf")]*(maxTime+1) for _ in range(n)] #best fees for node x and time t
        best[0][0]=passingFees[0]
        h=[(0,passingFees[0],0)]
        
        while h:
            t,c,x=heapq.heappop(h)
            
            if c>lowest[x] or c>best[x][t]: #if cost is lower only rthen go forward
                continue
            lowest[x]=min(lowest[x],c)
            
            if x==n-1: #if last node update ans
                ans=min(ans,c)
                continue
            
            for y,nt in edges_map[x]: #go through all edges starting from that node and if it is less than maxtime and new cost is less than curr add to heap and update best
                if t+nt<=maxTime and best[y][t+nt]>c+passingFees[y] and lowest[y]>c+passingFees[y]:
                    best[y][t+nt]=c+passingFees[y]
                    heapq.heappush(h,(t+nt,c+passingFees[y],y))
               
        if ans==float("inf"):
            return -1
        return ans