class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        '''
        need to use horners method
        (((z*p)+y)*p+x)*p = x*p+y*p^2+z*p^3 for a string xyz and k=3
        then we can just subtract z*p^4 whenever we want to remove z
        '''
        def val(x):
            return ord(x)-ord("a")+1
        pk=pow(power,k,modulo)
        curr=0
        n=len(s)
        ans=n
        for i in range(n-1,-1,-1):
            curr=(curr*power+val(s[i]))%modulo
            if i+k<n:
                curr=(curr-val(s[i+k])*pk)%modulo
            if curr==hashValue:
                ans=i
        return s[ans:ans+k]
        