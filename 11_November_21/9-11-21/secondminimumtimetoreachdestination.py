class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        #use heap and djikstras to find the n'th smallest path
        graph=defaultdict(list) #create adjacency list from edge list
        for u,v in edges:
            u-=1
            v-=1
            graph[u].append(v)
            graph[v].append(u)
        dist=[[float('inf')]*2 for _ in range(n)] #standard djikstra stuff
        dist[0][0]=0
        h=list()
        heapq.heappush(h,(0,0,0))
        change2=change*2 #to keep note of red or green light
        
        while h:
            d,curr,t=heapq.heappop(h) #d is the distance or time taken to reach the node, curr is the current node, t is the position that is 0th smallest 1th smalesst..
            if dist[curr][t]<d: #if the curr distance is less than the distance through the curr node don't do anything since distance is already smaller
                continue
            #check for red or green light
            if d%change2>=change:
                d=(d-(d%change2))+change2
            
            for v in graph[curr]:
                if dist[v][0]>d+time: #if curr smallest distance is greater, replace the 2nd smallest with it and the 1st smallest with d+time and push them in the heap
                    dist[v][1]=dist[v][0]
                    heapq.heappush(h,(dist[v][1],v,1))
                    dist[v][0]=d+time
                    heapq.heappush(h,(dist[v][0],v,0))
                else:
                    if dist[v][0]==d+time: #if the smallest is equal to curr dist do nothing
                        continue
                    if dist[v][1]>d+time: # if the curr distance is greater than 1st but smaller than second only change the second
                        dist[v][1]=d+time
                        heapq.heappush(h,(dist[v][1],v,1))
                
        return dist[n-1][1]