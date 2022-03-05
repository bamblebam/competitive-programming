class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        m=max(nums)
        factors=[[] for _ in range(m+2)]
        for i in range(1,m+1):
            j=i
            while j<=m:
                factors[j].append(i) #keeps track of factors like if i=40 then j=80,120,160,.. will have 40
                j+=i
        
        lookup=Counter()
        ans=0
        for x in nums:
            curr=gcd(x,k)
            ans+=lookup[k//curr]
            for y in factors[curr]:
                lookup[y]+=1
        return ans