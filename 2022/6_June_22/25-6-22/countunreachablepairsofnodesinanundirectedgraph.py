class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        use dfs to find the size of each connected component
        then just multiply the nodes
        can also use union findd but gets TLE
        """
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen=set()
        
        curr=1
        def dfs(node):
            nonlocal curr
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
                    curr+=1
        
        sets=list()
        
        for i in range(n):
            if i not in seen:
                curr=1
                dfs(i)
                sets.append(curr)
        
        values=list(accumulate(sets))
        m=len(values)
        ans=0
        for i in range(m):
            ans+=sets[i]*(values[-1]-values[i])
        
        return ans
            
        