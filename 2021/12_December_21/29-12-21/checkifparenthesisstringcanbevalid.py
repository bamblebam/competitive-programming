class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #just check if the string can be be valid 2 times, once normally and the other in reverse
        #if the lock is 0 at that pos then it can be considered as any type of bracket so just add to the count
        n=len(s)
        if n&1:
            return False
        
        count=0
        for c,i in zip(s,locked):
            if i=='0' or c=="(":
                count+=1
            elif c==")":
                count-=1
            if count<0:
                return False
        
        count=0
        for c,i in zip(reversed(s),reversed(locked)):
            if i=="0" or c==")":
                count+=1
            elif c=="(":
                count-=1
            if count<0:
                return False
        
        return True
                
        