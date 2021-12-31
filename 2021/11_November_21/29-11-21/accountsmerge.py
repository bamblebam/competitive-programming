class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #use dfs on graph
        #the emails are connected components
        
        #names dict to store which email has what name
        names=dict()
        #created graph
        graph=defaultdict(set)
        for account in accounts:
            name=account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                names[email]=name
        
        components,seen ,i=defaultdict(list),set(),0
        
        #go through all connected components for an email and add them to a dict
        def dfs(node,i):
            components[i].append(node)
            seen.add(node)
            for neib in graph[node]:
                if neib not in seen:
                    dfs(neib,i)
        
        for email,val in graph.items():
            if email not in seen:
                dfs(email,i)
                i+=1
        
        return [[names[val[0]]]+sorted(val) for k,val in components.items()]
        