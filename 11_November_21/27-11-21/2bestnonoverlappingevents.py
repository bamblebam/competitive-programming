class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        #use sweep line algos, can also be done with heap and binary search
        #put all events in list with start/end, type and value and sort it
        #go through all the events if it is start update ans, if end update maxPrefix
        
        ans=0 #this is maximum value including current box
        maxPrefix=0 #this is value of maximum possible box before the current box
        
        ev=list()
        for start,end,val in events:
            ev.append((start,1,val))
            ev.append((end+1,-1,val))
        ev.sort() #sorting the events, 1 is start, -1 is end
        
        for x,t,val in ev:
            if t==1:
                ans=max(ans,maxPrefix+val) #if it is start update ans, it can either be the curr ans or the curr val with the maxPrefix
            else:
                maxPrefix=max(maxPrefix,val) #when the event ends it will be compared with the maxPrefix and if it is bigger it will be updated.
        
        return ans
        