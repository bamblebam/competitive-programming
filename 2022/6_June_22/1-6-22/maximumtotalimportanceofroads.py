class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        c=Counter()
        for i in range(n):
            c[i]=0
        for a,b in roads:
            c[a]+=1
            c[b]+=1
        
        sorted_cities=list(reversed(list(x[1] for x in sorted((v,k) for k,v in c.items()))))
        city_values={sorted_cities[i]:n-i for i in range(n)}
        ans=0
        for a,b in roads:
            ans+=city_values[a]+city_values[b]
        
        return ans