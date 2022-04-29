"""
use DSU to keep track of all the letters that are connected to each other
any letter in this connected grp can be swapped with any other letter in the same group
use union to make the groups then sort all letters of a particular grp
iterate through all spots in range n and put the smallest letter and pop it

can also be done using dfs
"""

class DSU:
    def __init__(self,size):
        self.groups=[0]*size
        for i in range(size):
            self.groups[i]=i
        
    
    def ufind(self,a):
        if self.groups[a]!=a:
            self.groups[a]=self.ufind(self.groups[a])
        return self.groups[a]
    
    def uunion(self,a,b):
        fa=self.ufind(a)
        fb=self.ufind(b)
        if fa==fb:
            return False
        
        self.groups[fa]=fb
        
        return True
        
    

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        dsu=DSU(n)
        ans=""
        letter_map=defaultdict(list)
        
        for x,y in pairs:
            dsu.uunion(x,y)
        
        for i,x in enumerate(dsu.groups):
            letter_map[dsu.ufind(x)].append(s[i])
        
        for k,v in letter_map.items():
            letter_map[k]=list(sorted(v))
        
        for i in range(n):
            x=dsu.ufind(i)
            ans+=letter_map[x].pop(0)
        
        return ans