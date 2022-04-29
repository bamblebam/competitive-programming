"""
use dsu to keep track of the diff components
all components in same graph are connected
check if for any node any of the nodes its connected to belong to same grp if yes then it cant be bipartite
after that do a union with the first edge it connects to and the jth edge
"""
class DSU:
    def __init__(self,size):
        self.groups=[i for i in range(size)]
    
    def ufind(self,a):
        if self.groups[a]!=a:
            self.groups[a]=self.ufind(self.groups[a])
        return self.groups[a]
    
    def uunion(self,a,b):
        fa=self.ufind(a)
        fb=self.ufind(b)
        if fa!=fb:
            self.groups[fa]=fb
    
        
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        dsu=DSU(n)
        for i in range(n):
            x=dsu.ufind(i)
            for j in graph[i]:
                if dsu.ufind(j)==x:
                    return False
                dsu.uunion(graph[i][0],j)
        return True