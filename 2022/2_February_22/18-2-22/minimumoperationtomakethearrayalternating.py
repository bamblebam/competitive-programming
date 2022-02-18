class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        '''
        didn't understand much
        take counters of odd and even indices and keep track of how many times a num appears at those indices
        if the most appeared num in odd and even indices is different then just replace the remaining nums with them
        if they are the same check for both cases when you take odd or even num
        '''
        odd=Counter()
        even=Counter()
        for i,x in enumerate(nums):
            if i%2:
                odd[x]+=1
            else:
                even[x]+=1
        
        et=sum(even.values())
        ot=sum(odd.values())
        ev=list(sorted(even.items(),key=lambda x:(-x[1],x[0])))
        ov=list(sorted(odd.items(),key=lambda x:(-x[1],x[0])))
        
        if not ov:
            return 0
        
        if ev[0][0]==ov[0][0]:
            poss=float("inf")
            if len(ov)>1:
                poss=min(poss,et-ev[0][1]+ot-ov[1][1])
            else:
                poss=min(poss,et-ev[0][1]+ot)
            if len(ev)>1:
                poss=min(poss,et-ev[1][1]+ot-ov[0][1])
            else:
                poss=min(poss,et+ot-ov[0][1])
            return poss
        else:
            return et-ev[0][1]+ot-ov[0][1]
                