class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        #determine all possible button combs and then just find the score
        #find comb for dividing by 99 and 60
        cands=list()
        if targetSeconds<100:
            cands.append(targetSeconds)
            x=targetSeconds%60
            if x==0:
                x="00"
            elif x<10:
                x="0"+str(x)
            cands.append(int(str(targetSeconds//60)+str(x)))
        else:
            mins=targetSeconds//60
            if targetSeconds%60==0:
                cands.append(int(str(mins)+"00"))
            if targetSeconds%60+60<100:
                cands.append(int(str(mins-1)+str(targetSeconds%60+60)))
            x=targetSeconds%60
            if x==0:
                    x="00"
            elif x<10:
                x="0"+str(x)
            cands.append(int(str(mins)+str(x)))
            
            
        
        ans=float("inf")
        for cand in cands:
            x=str(cand)
            if len(x)>4:
                continue
            count=0
            curr=startAt
            for i,c in enumerate(x):
                if int(c)==curr:
                    count+=pushCost
                else:
                    count+=pushCost+moveCost
                    curr=int(c)
            ans=min(count,ans)
        
        return ans