class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        #use djikstras to find the shortest path from main server to all data server, the weights of the path are all 1
        #then just check how many signals are sent and the final time the last signal nis sent for a particular node
        #this time + the timetaken to complete an entire msg cycle is the longest time for that particular server
        #do this for all servers and the max time is your ans
        graph=defaultdict(list)
        n=len(patience)
        
        #make a graph
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        #djikstras
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
        
        #calculate max time
        ans=0
        for i in range(1,n):
            signals_sent=math.ceil(2*dist[i]/patience[i]) #the amount of signals sent by this server
            time_sent=(signals_sent-1)*patience[i] #the time when the final signal is sent
            final_time=time_sent+dist[i]*2 #the final time the server is running
            ans=max(ans,final_time)
        
        return ans+1