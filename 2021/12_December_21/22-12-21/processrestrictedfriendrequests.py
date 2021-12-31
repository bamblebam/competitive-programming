class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        #use union find for this
        #create parent arr and ufind func
        #go through each request and find both parents, if same they belong to same grp
        #else go through all restrictions and find their parents if there is any match between request and restriction parent it is false since they cannot be in different grps
        #if they lie in same grp the parents of the 2 requests need to be equalized
        parents=[i for i in range(n)]
        
        def ufind(x):
            if x!=parents[x]:
                parents[x]=ufind(parents[x])
            return parents[x]
        
        ans=[0]*len(requests)
        
        for i,(x,y) in enumerate(requests):
            left=ufind(x)
            right=ufind(y)
            if left==right:
                ans[i]=True
                continue
            
            flag=True
            for rx,ry in restrictions:
                rleft=ufind(rx)
                rright=ufind(ry)
                if (rleft==left and rright==right) or (rleft==right and rright==left):
                    flag=False
                    break
            
            ans[i]=flag
            if flag:
                parents[left]=parents[right]
              
        return ans