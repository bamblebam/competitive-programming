class Solution:
    def minimumTime(self, s: str) -> int:
        '''
        use dp sorta
        if at a particular pos i it is 1 it can either take 2 or i+1 points to move the car
        get the minimum of it in a prefix sum kinda way
        do it for both left and right side for 1,2,3..n elements
        then just take the sum of the left and right ones
        '''
        def helper(s):
            n=len(s)
            prefix=[0]*(n+1)
            for i in range(n):
                curr=int(s[i])
                if curr==1:
                    prefix[i+1]=prefix[i]+2
                else:
                    prefix[i+1]=prefix[i]
                prefix[i+1]=min(prefix[i+1],i+1)
            return prefix
        
        prefix=helper(s)
        suffix=helper(s[::-1])[::-1]
        
        ans=float("inf")
        for l,r in zip(prefix,suffix):
            ans=min(ans,l+r)
        
        return ans