class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        """
        use djikstras 3 times
        1 to find all dists from node to src1
        1 to find all routes from node to src2
        1 to find all routes from dest to node
        then just add those 
        like dist from src1 to a common node + dist from src2 to a common node + dist from dest to that common node
        maintain 2 graphs one normal and one reverse for dest to common node
        we are bruteforcing all the common nodes and checking if it is possiblr to get a subgraph
        """
        e=defaultdict(list)
        er=defaultdict(list)
        inf=float('inf')
        
        for u,v,w in edges:
            e[u].append((v,w))
            er[v].append((u,w))
        
        def helper(e,start):
            best=[inf]*n
            best[start]=0
            h=list()
            heappush(h,(0,start))
            
            while h:
                dist,node=heappop(h)
                if dist>best[node]:
                    continue
                for v,w in e[node]:
                    if best[v]>dist+w:
                        best[v]=dist+w
                        heappush(h,(best[v],v))
            
            return best
        
        d1=helper(e,src1)
        d2=helper(e,src2)
        d3=helper(er,dest)
        
        ans=inf
        
        for i in range(n):
            ans=min(ans,d1[i]+d2[i]+d3[i])
        
        if ans>=inf:
            return -1
        return ans