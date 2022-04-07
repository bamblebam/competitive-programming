class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        create separate rules for separate conditions
        1. All numbers are same
        2. 2 numbers are same
        3. All numbers are different
        """
        n=103
        mod=10**9+7
        count=[0]*n
        ans=0
        
        for num in arr:
            count[num]+=1
        
        i=target//3
        if i*3==target:
            ans+=math.comb(count[i],3)
            ans%=mod
        
        for i in range(n):
            j=target-i*2
            if j!=i and 0<=j<n:
                ans+=math.comb(count[i],2)*count[j]
                ans%=mod
        
        for i in range(n):
            for j in range(i+1,n):
                k=target-i-j
                if k>j and 0<=k<n:
                    ans+=count[i]*count[j]*count[k]
                    ans%=mod
        
        return ans%mod
                    
            