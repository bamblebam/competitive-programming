class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        if len(edges)==0:
            return [[] for _ in range(n)]
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        ans=[[] for _ in range(n)]
        def bfs(node):
            seen={node}
            queue=deque([node])
            while queue:
                x=queue.pop()
                if node!=x:
                    ans[x].append(node)
                for child in graph[x]:
                    if child not in seen:
                        seen.add(child)
                        queue.append(child)
        for i in range(n):
            bfs(i)
        return ans
                        
                    
                