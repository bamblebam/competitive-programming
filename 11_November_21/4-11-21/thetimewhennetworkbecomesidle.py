class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph=defaultdict(list)
        n=len(patience)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        dist=[float('inf')]*n
        dist[0]=0
        visited=set()
        queue=list()
        heappush(queue,(0,0))
        while queue:
            curr_weight,curr_node=heappop(queue)
            visited.add(curr_node)
            for next_node in graph[curr_node]:
                if next_node not in visited and curr_weight+1<dist[next_node]:
                    dist[next_node]=curr_weight+1
                    heappush(queue,(dist[next_node],next_node))
        
        ans=0
        for i in range(1,n):
            signals_sent=math.ceil(2*dist[i]/patience[i])
            time_sent=(signals_sent-1)*patience[i]
            # print(signals_sent,time_sent,dist[i])
            final_time=time_sent+dist[i]*2
            ans=max(ans,final_time)
        
        return ans+1