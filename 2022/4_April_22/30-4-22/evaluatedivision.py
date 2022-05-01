class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        use floyd warshall to store the different a/b,c/d pairs
        for each a/c=a/b * b/c use floyd warshall to populate those pairs
        """
        keys=dict()
        
        def add_keys(x):
            if x not in keys:
                keys[x]=len(keys)
        
        def get_keys(x):
            if x not in keys:
                return None
            return keys[x]
        
        for a,b in equations:
            add_keys(a)
            add_keys(b)
        
        n=len(keys)
        v=[[None]*n for _ in range(n)]
        
        for (a,b),x in zip(equations,values):
            a=get_keys(a)
            b=get_keys(b)
            v[a][b]=x
            v[b][a]=1./x
            v[a][a]=1.
            v[b][b]=1.
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if v[i][j] is None and v[i][k] is not None and v[k][j] is not None:
                        v[i][j]=v[i][k]*v[k][j]
        
        ans=list()
        for c,d in queries:
            c=get_keys(c)
            d=get_keys(d)
            if c is not None and d is not None and v[c][d] is not None:
                ans.append(v[c][d])
            else:
                ans.append(-1.)
        
        return ans