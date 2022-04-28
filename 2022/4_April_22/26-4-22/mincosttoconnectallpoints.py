class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        use prims algo to find the mst
        keep a min dist list to keep track of the min dist to all nodes from the curr node
        keep a list seen to keep track of all the nodes visited yet
        can also use kruskals with DSU
        """
        n=len(points)
        mst_edges=0
        mst_cost=0
        
        seen=[False]*n
        
        min_dist=[float('inf')]*n
        min_dist[0]=0
        
        while mst_edges<n:
            curr_node=-1
            curr_dist=float('inf')
            
            for node in range(n):
                if not seen[node] and curr_dist>min_dist[node]:
                    curr_dist=min_dist[node]
                    curr_node=node
            
            mst_cost+=curr_dist
            mst_edges+=1
            seen[curr_node]=True
            
            for next_node in range(n):
                weight=abs(points[curr_node][0]-points[next_node][0])+abs(points[curr_node][1]-points[next_node][1])
                if not seen[next_node] and min_dist[next_node]>weight:
                    min_dist[next_node]=weight
            
        return mst_cost