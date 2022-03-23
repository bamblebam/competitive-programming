class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        n=len(logs)
        digs=list()
        lets=list()
        for log in logs:
            x=log.split(' ')
            idx=x[0]
            cont=" ".join(x[1:])
            x=(cont,idx)
            digits=any(i.isdigit() for i in cont)
            if digits:
                digs.append(x)
            else:
                lets.append(x)
        
        lets.sort()
        ans=lets+digs
        res=[" ".join((y,x)) for x,y in ans]
        return res