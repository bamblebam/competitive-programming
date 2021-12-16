class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #can also be done using DFS and memoization
        #some topological sort BS
        #trim the leaf nodes one by one until you reach the 2 centroid nodes
        edges_map=defaultdict(set)
        for u,v in edges:
            edges_map[u].add(v)
            edges_map[v].add(u)
        
        if n<=2:
            return [i for i in range(n)]
        
        leaves=list()
        for i in range(n):
            if len(edges_map[i])==1:
                leaves.append(i)
                
        remaining_nodes=n
        while remaining_nodes>2:
            new_leaves=list()
            remaining_nodes-=len(leaves)
            #remove the current leaves frim the tree
            while leaves:
                leaf=leaves.pop()
                neighbor=edges_map[leaf].pop() #remove the edges ??? remove the connection from both u and v part of dict
                edges_map[neighbor].remove(leaf)
                if len(edges_map[neighbor])==1:
                    new_leaves.append(neighbor)
            
            leaves=new_leaves
        
        return leaves