# use union find to link all the primes that have been found out by using sieve of erasthenoses by using uunion.
# then check if the ufind of nums and sorted nums (snums) actually have the same parent, if not then the number can never be put in the correct position
# as nothing can swap with it, so it is wrong.

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = max(nums)
        snums = sorted(nums)
        parents = dict()
        primes = [list() for _ in range(mx+1)]

        def ufind(x):
            if x not in parents:
                parents[x] = x
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            parents[ua] = ub

        for i in range(2, mx+1):
            if len(primes[i]) == 0:
                primes[i].append(i)
                j = 2*i
                while j <= mx:
                    primes[j].append(i)
                    j += i

        for x in nums:
            for y in primes[x][1:]:
                uunion(primes[x][0], y)

        for a, b in zip(nums, snums):
            if ufind(primes[a][0]) != ufind(primes[b][0]):
                return False

        return True
