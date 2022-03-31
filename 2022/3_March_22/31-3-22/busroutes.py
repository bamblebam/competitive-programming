class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Use BFS
        instead of using the stops as nodes and busses as edges
        use the busses as nodes and the edge will be if the routes of 2 busses intersect
        then just create the graph and use BFS
        """
        if source==target:
            return 0
        
        routes=list(map(set,routes))
        graph=defaultdict(set)
        
        for i,r1 in enumerate(routes):
            for j,r2 in enumerate(routes[i+1:]):
                if any(r in r2 for r in r1):
                    graph[i].add(j+i+1)
                    graph[j+i+1].add(i)
        
        seen,targets=set(),set()
        for node,route in enumerate(routes):
            if source in route:
                seen.add(node)
            if target in route:
                targets.add(node)
        
        queue=deque([(node,1) for node in seen])
        
        while queue:
            node,distance=queue.popleft()
            if node in targets:
                return distance
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei,distance+1))
        
        return -1