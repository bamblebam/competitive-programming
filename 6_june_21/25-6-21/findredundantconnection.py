class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(x for x in range(n))

        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]

        def uunion(x, y):
            parent[ufind(x)] = ufind(y)

        for u, v in edges:
            u -= 1
            v -= 1
            if ufind(u) == ufind(v):
                return [u+1, v+1]
            uunion(u, v)
