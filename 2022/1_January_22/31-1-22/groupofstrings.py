class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        #some union find bs
        # tc is O(n*26)
        parents=dict()
        
        def ufind(x):
            if x not in parents:
                parents[x]=x
            if parents[x]!=x:
                parents[x]=ufind(parents[x])
            return parents[x]
        
        def uunion(a,b):
            ua=ufind(a)
            ub=ufind(b)
            parents[ua]=ub
        
        seen=Counter()
        oneof=dict()
        
        for word in words:
            mask=0
            for letter in word:
                mask|=1<<(ord(letter)-ord("a"))
            seen[mask]+=1
            
            for i in range(26):
                if mask&(1<<i)==0:
                    nmask=mask|(1<<i)
                else:
                    nmask=mask^(1<<i)
                    if nmask in oneof:
                        uunion(mask,oneof[nmask])
                    else:
                        oneof[nmask]=mask
                
                if nmask in seen:
                    uunion(mask,nmask)
        
        g=Counter()
        best=0
        for key in seen:
            u=ufind(key)
            g[u]+=seen[key]
            best=max(best,g[u])
        
        return [len(g),best]
    
