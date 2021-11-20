class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # Use union find to link all the components and find the largest connected component.
        # Use prime factor decomposition to create dict where prime number keys point to their multiples
        # Use union find on that
        
        n=len(nums)
        #Union Find
        parents=list(range(n))
        
        def ufind(x):
            if x!=parents[x]:
                parents[x]=ufind(parents[x])
            return parents[x]
        
        def uunion(x,y):
            xr,yr=ufind(x),ufind(y)
            parents[xr]=yr
            
        #prime nums
        def primes(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return primes(n//i)|set([i])
            return set([n])
        #put the prime nums in a dict
        #primes func will give you all the prime nums that divide a number, add them to the dict 
        primes_dict=defaultdict(list)
        for i,num in enumerate(nums):
            prime_nums=primes(num)
            for j in prime_nums:
                primes_dict[j].append(i)
        #use union on all the values
        for k,v in primes_dict.items():
            for i in range(len(v)-1):
                uunion(v[i],v[i+1])
        #ufind on all the nums to find which parent occurs most of the time
        return max(Counter([ufind(x) for x in range(n)]).values())