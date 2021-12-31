class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        #use dfs for this
        #add all edges to a map and then run dfs
        #if node is 0 update the ans, s is the set of all unique visited nodes
        edges_map=defaultdict(set)
        for u,v,t in edges:
            edges_map[u].add((v,t))
            edges_map[v].add((u,t))
        
        ans=0
        def helper(v,s,left):
            nonlocal ans
            if v==0:
                total=0
                for x in s:
                    total+=values[x]
                ans=max(total,ans)
            for u,t in edges_map[v]: #this goes through all nodes that one can visit from v and checks if they will utilize less time than maxTime
                if left-t>=0:
                    helper(u,s|set([u]),left-t)
        
        helper(0,set([0]),maxTime)
        return ans

        
            
        