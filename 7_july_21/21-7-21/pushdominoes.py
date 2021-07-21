class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        force=[0]*n
        curr=0
        for i in range(n):
            if dominoes[i]=='R':
                curr=n
            elif dominoes[i]=='L':
                curr=0
            else:
                curr=max(curr-1,0)
            force[i]+=curr
        curr=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='L':
                curr=n
            elif dominoes[i]=='R':
                curr=0
            else:
                curr=max(curr-1,0)
            force[i]-=curr
        return "".join(['.' if force[i]==0 else 'R' if force[i]>0 else 'L' for i in range(n)])
                
                