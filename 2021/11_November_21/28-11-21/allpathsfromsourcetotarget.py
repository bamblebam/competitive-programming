class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #use dfs and backtracking to find all possible paths
        
        n=len(graph)
        ans=list()
        
        def dfs(node,path):
            if node==n-1: #if node is last append path to ans
                ans.append(path[:])
            
            for res in graph[node]: #for every node that the curr node taks you add it to path perform dfs and remove it (backtrack)
                path.append(res)
                dfs(res,path)
                path.pop()
            
        dfs(0,[0])
        return ans
