class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #use prefix and suffix arrays to keep track of the distance from the people sitting to the left and right of a seat
        #then just go over the seats and get the maximum ans
        n=len(seats)
        
        left=[0]
        for i in range(n):
            if seats[i]==1:
                left.append(0)
            else:
                left.append(left[-1]+1)
                
        right=[0]
        for i in range(n-1,-1,-1):
            if seats[i]==1:
                right.append(0)
            else:
                right.append(right[-1]+1)
        right.reverse()
        
        left=left[1:]
        right=right[:-1]
        
        if right[-1]!=0:
            right[-1]=float("inf")
        if left[0]!=0:
            left[0]=float("inf")
        
        ans=0
        for i in range(n):
            if seats[i]==1:
                continue
            ans=max(ans,min(left[i],right[i]))
        
        return ans