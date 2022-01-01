class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        #use 2 pointers for alice and bob
        #one from start and other from back
        #check whether they have enough water else update ans and move them ahead
        n=len(plants)
        ans=0
        i,j=0,n-1
        a,b=capacityA,capacityB
        
        while i<=j:
            if i==j:
                if plants[i]>max(a,b):
                    ans+=1
                return ans
            if plants[i]>a:
                a=capacityA
                ans+=1
            if plants[i]<=a:
                a-=plants[i]
                i+=1
                
            if plants[j]>b:
                b=capacityB
                ans+=1
            if plants[j]<=b:
                b-=plants[j]
                j-=1
                
        return ans
            