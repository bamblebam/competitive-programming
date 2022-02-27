class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        '''
        floyd warshall + bit mask
        use floyd warshall to get the minimum path from each node to every other node
        then use bitmask func to check if all nodes have been visited
        if not use loop to go the next node from that node
        do this for each node as starting node
        TC = 2^n*n^2
        '''
        n=len(graph)
        dist=[[float("inf")]*n for _ in range(n)]
        
        for i,edges in enumerate(graph):
            dist[i][i]=0
            for edge in edges:
                dist[i][edge]=1
                dist[edge][i]=1
        #floyd warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        
        ans=float("inf")
        
        @lru_cache(None)
        def visit(node,visited):
            if visited==(1<<n)-1:
                return 0
            best=float("inf")
            for i in range(n):
                if (1<<i)&visited==0:
                    best=min(best,visit(i,visited|1<<i)+dist[node][i])
            return best
        
        for i in range(n):
            ans=min(ans,visit(i,1<<i))
        
        return ans