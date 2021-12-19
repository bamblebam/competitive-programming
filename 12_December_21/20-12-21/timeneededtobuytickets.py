class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        #check for all the tickets if they are before k they will take min(target,all) tickets and if after they will take min(target-1),all tickets
        target=tickets[k]
        ans=0
        for i,x in enumerate(tickets):
            if i<k:
                ans+=min(x,target)
            if i>k:
                ans+=min(x,target-1)
        ans+=target
        return ans