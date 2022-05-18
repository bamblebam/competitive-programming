class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me
        """
        graph=defaultdict(list)
        lowestRank=[0]*n
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(rank,curr,prev):
            lowestRank[curr]=rank
            res=[]
            for nei in graph[curr]:
                if nei==prev:
                    continue
                if not lowestRank[nei]:
                    res+=dfs(rank+1,nei,curr)
                lowestRank[curr]=min(lowestRank[curr],lowestRank[nei])
                if lowestRank[nei]>=rank+1:
                    res.append([curr,nei])
            return res
        
        return dfs(1,0,-1)
    