class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        #add all indices for a num in dict
        #iterate over the indices list and get the ans for 1st idx in it
        #then as you move right all indices on the right will be subtracted by delta and all on left will be added by delta
        #that will be new total because as we go ahead in list the distance to the right indices will reduce and left will increase
        indices=defaultdict(list)
        for i,num in enumerate(arr):
            indices[num].append(i)

        n=len(arr)
        ans=[0]*n
        
        for v in indices.values():
            m=len(v)
            l,r=0,m-1
            total=0
            
            for x in v:
                total+=x-v[0]
            ans[v[0]]=total
            
            for prev,curr in zip(v,v[1:]):
                l+=1
                delta=curr-prev
                total+=l*delta-r*delta
                r-=1
                ans[curr]=total
                
        return ans
                
        
        