class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        n=len(bank)
        m=len(bank[0])
        
        count=Counter()
        for i in range(n):
            for j in range(m):
                if bank[i][j]=="1":
                    count[i]+=1
                    
        vals=list(count.values())
        k=len(vals)
        if k<2:
            return 0
        
        for i in range(1,k):
            ans+=vals[i-1]*vals[i]
        
        return ans