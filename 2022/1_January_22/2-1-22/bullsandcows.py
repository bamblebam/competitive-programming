class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls,cows=0,0
        indices=set()
        count=Counter(secret)
        
        #finding bulls
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                indices.add(i)
                count[secret[i]]-=1
        
        #finding cows
        for i in range(len(secret)):
            if i in indices:
                continue
            if guess[i] not in secret:
                continue
            if count[guess[i]]>0:
                count[guess[i]]-=1
                cows+=1
        
        return f"{bulls}A{cows}B"
            