class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        #put both items and queries in a single list and sort it on the basis of price, use a type var to differentiate between the 2
        #go through each event and update the max beauty if it is an item, if a query update the ans arr with the curr max
        #since everything is sorted it works
        events=list()
        for i,q in enumerate(queries):
            events.append([q,1,i])
        for p,b in items:
            events.append([p,0,b])
        events.sort()
        mx=0
        ans=[0]*len(queries)
        for _,t,x in events:
            if t==0:
                mx=max(mx,x)
            else:
                ans[x]=mx
        return ans