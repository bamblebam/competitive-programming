class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #use line sweep algorithm
        #add all entry and exit points to events and sort them
        #then at each point keep track of how many people are in the car
        #if the number of passangers is more than n return False
        events=list()
        for n,l,r in trips:
            events.append((r,-1,n))
            events.append((l,1,n))
        events.sort()
        count=0
        for x,t,n in events:
            if t==1:
                count+=n
            else:
                count-=n
            if count>capacity:
                return False
        return True